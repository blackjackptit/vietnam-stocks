"""
Real-time WebSocket server for live dashboard updates
Pushes data to dashboard instantly when new scans complete
"""

import asyncio
import websockets
import json
import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

connected_clients = set()

class ScanFileHandler(FileSystemEventHandler):
    """Watch for new scan files and broadcast to connected clients"""

    def __init__(self, loop):
        self.loop = loop
        self.last_file = None

    def on_created(self, event):
        if event.src_path.endswith('.json') and 'scan_' in event.src_path:
            # New scan file created
            asyncio.run_coroutine_threadsafe(
                self.broadcast_new_scan(event.src_path),
                self.loop
            )

    def on_modified(self, event):
        if event.src_path.endswith('.json') and 'scan_' in event.src_path:
            # Scan file updated
            if event.src_path != self.last_file:
                self.last_file = event.src_path
                asyncio.run_coroutine_threadsafe(
                    self.broadcast_new_scan(event.src_path),
                    self.loop
                )

    async def broadcast_new_scan(self, filepath):
        """Read scan file and broadcast to all connected clients"""
        try:
            # Wait a moment for file to be fully written
            await asyncio.sleep(0.5)

            with open(filepath, 'r') as f:
                data = json.load(f)

            message = json.dumps({
                'type': 'scan_update',
                'data': data,
                'timestamp': time.time()
            })

            print(f"📡 Broadcasting new scan: {Path(filepath).name}")
            print(f"   Connected clients: {len(connected_clients)}")

            # Send to all connected clients
            if connected_clients:
                await asyncio.gather(
                    *[client.send(message) for client in connected_clients],
                    return_exceptions=True
                )
                print(f"   ✅ Sent to {len(connected_clients)} clients")

        except Exception as e:
            print(f"   ❌ Error broadcasting: {e}")


async def handler(websocket):
    """Handle WebSocket connections"""
    connected_clients.add(websocket)
    print(f"🔌 Client connected. Total clients: {len(connected_clients)}")

    try:
        # Send latest scan data immediately on connect
        latest_scan = get_latest_scan()
        if latest_scan:
            await websocket.send(json.dumps({
                'type': 'scan_update',
                'data': latest_scan,
                'timestamp': time.time()
            }))
            print(f"   📤 Sent initial data to client")

        # Keep connection alive
        async for message in websocket:
            # Handle ping/pong or other messages
            if message == 'ping':
                await websocket.send('pong')

    except websockets.exceptions.ConnectionClosed:
        print(f"🔌 Client disconnected")
    finally:
        connected_clients.remove(websocket)
        print(f"   Total clients: {len(connected_clients)}")


def get_latest_scan():
    """Get the most recent scan file"""
    try:
        output_dir = Path('output')
        if not output_dir.exists():
            return None

        scan_files = list(output_dir.glob('scan_*.json'))
        if not scan_files:
            return None

        latest_file = max(scan_files, key=lambda p: p.stat().st_mtime)

        with open(latest_file, 'r') as f:
            return json.load(f)

    except Exception as e:
        print(f"❌ Error reading latest scan: {e}")
        return None


async def start_websocket_server():
    """Start WebSocket server"""
    print("=" * 70)
    print("🚀 Real-time WebSocket Server")
    print("=" * 70)
    print(f"📡 WebSocket: ws://localhost:8765")
    print(f"📁 Watching: output/")
    print(f"🔄 Dashboard will update instantly when new scans complete")
    print("=" * 70)
    print()

    async with websockets.serve(handler, "localhost", 8765):
        print("✅ WebSocket server started")
        print("⏳ Waiting for connections and scan updates...\n")
        await asyncio.Future()  # Run forever


def start_file_watcher(loop):
    """Start watching output directory for new scan files"""
    event_handler = ScanFileHandler(loop)
    observer = Observer()
    observer.schedule(event_handler, path='output', recursive=False)
    observer.start()
    print("👁️  File watcher started\n")
    return observer


async def main():
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)

    # Get event loop
    loop = asyncio.get_event_loop()

    # Start file watcher
    observer = start_file_watcher(loop)

    try:
        # Start WebSocket server
        await start_websocket_server()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
        observer.stop()
        observer.join()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
