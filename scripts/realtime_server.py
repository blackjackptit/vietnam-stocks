#!/usr/bin/env python3
"""
Real-time Server with Server-Sent Events (SSE)
No dependencies needed - uses only standard library!
"""

import http.server
import socketserver
import json
import os
import time
import threading
from pathlib import Path
from datetime import datetime

PORT = 8888
latest_scan = None
scan_lock = threading.Lock()


class RealtimeHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with SSE support"""

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_POST(self):
        """Handle POST requests"""

        # Save watchlist endpoint
        if self.path == '/api/watchlist':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                watchlist = json.loads(post_data.decode('utf-8'))

                # Save to file
                with open('watchlist.json', 'w') as f:
                    json.dump(watchlist, f, indent=2)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'count': len(watchlist)}).encode())

                print(f"💾 Watchlist saved: {len(watchlist)} stocks")
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Save automation state endpoint
        elif self.path == '/api/automation':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                automation_state = json.loads(post_data.decode('utf-8'))

                # Save to file
                with open('automation_config.json', 'w') as f:
                    json.dump(automation_state, f, indent=2)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode())

                status = "ENABLED" if automation_state.get('enabled') else "DISABLED"
                print(f"🤖 Automated trading {status}")
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Default: method not allowed
        self.send_error(405)

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests"""

        # SSE endpoint
        if self.path == '/stream':
            self.handle_sse()
            return

        # Latest scan endpoint
        elif self.path == '/api/latest':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            with scan_lock:
                if latest_scan:
                    self.wfile.write(json.dumps(latest_scan).encode())
                else:
                    self.wfile.write(json.dumps({'error': 'No data yet'}).encode())
            return

        # Stock database endpoint
        elif self.path == '/api/stocks':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            try:
                from src.stock_data import STOCK_LISTS
                self.wfile.write(json.dumps(STOCK_LISTS).encode())
            except Exception as e:
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Watchlist endpoint - GET
        elif self.path == '/api/watchlist':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            try:
                watchlist_file = Path('watchlist.json')
                if watchlist_file.exists():
                    with open(watchlist_file, 'r') as f:
                        watchlist = json.load(f)
                    self.wfile.write(json.dumps(watchlist).encode())
                else:
                    self.wfile.write(json.dumps([]).encode())
            except Exception as e:
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Automation state endpoint - GET
        elif self.path == '/api/automation':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            try:
                automation_file = Path('automation_config.json')
                if automation_file.exists():
                    with open(automation_file, 'r') as f:
                        config = json.load(f)
                    self.wfile.write(json.dumps(config).encode())
                else:
                    self.wfile.write(json.dumps({'enabled': False}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Stock names endpoint - GET
        elif self.path == '/api/stock-names':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            try:
                stock_names_file = Path('stock_names.json')
                if stock_names_file.exists():
                    with open(stock_names_file, 'r') as f:
                        names = json.load(f)
                    self.wfile.write(json.dumps(names).encode())
                else:
                    self.wfile.write(json.dumps({}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        # Serve files
        else:
            super().do_GET()

    def handle_sse(self):
        """Handle Server-Sent Events stream"""
        self.send_response(200)
        self.send_header('Content-type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Accel-Buffering', 'no')
        self.end_headers()

        try:
            # Send initial data
            with scan_lock:
                if latest_scan:
                    self.send_event('scan_update', latest_scan)

            # Keep connection alive
            while True:
                time.sleep(10)
                # Send heartbeat
                self.wfile.write(b':heartbeat\n\n')
                self.wfile.flush()

        except (BrokenPipeError, ConnectionResetError):
            pass

    def send_event(self, event_type, data):
        """Send SSE event"""
        message = f"event: {event_type}\ndata: {json.dumps(data)}\n\n"
        self.wfile.write(message.encode())
        self.wfile.flush()

    def log_message(self, format, *args):
        """Reduce logging verbosity"""
        if args and isinstance(args[0], str) and '/stream' not in args[0]:
            super().log_message(format, *args)
        elif not args or not isinstance(args[0], str):
            super().log_message(format, *args)


def watch_for_scans():
    """Watch for new scan files and update latest_scan"""
    global latest_scan

    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    last_mtime = 0

    print("👁️  Watching for scan updates...")

    while True:
        try:
            # Find latest scan file
            scan_files = list(output_dir.glob('scan_*.json'))
            if scan_files:
                latest_file = max(scan_files, key=lambda p: p.stat().st_mtime)
                current_mtime = latest_file.stat().st_mtime

                if current_mtime > last_mtime:
                    # New scan detected
                    with open(latest_file, 'r') as f:
                        new_data = json.load(f)

                    with scan_lock:
                        latest_scan = new_data

                    print(f"📊 New scan detected: {latest_file.name}")
                    print(f"   Timestamp: {datetime.now().strftime('%H:%M:%S')}")

                    last_mtime = current_mtime

            time.sleep(2)  # Check every 2 seconds

        except Exception as e:
            print(f"Error watching scans: {e}")
            time.sleep(5)


def main():
    os.chdir(Path(__file__).parent)

    # Start file watcher thread
    watcher_thread = threading.Thread(target=watch_for_scans, daemon=True)
    watcher_thread.start()

    # Start HTTP server
    Handler = RealtimeHandler

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/dashboard_realtime.html"

        print("=" * 70)
        print(f"🚀 Real-time Vietnamese Stock Monitor Dashboard")
        print("=" * 70)
        print(f"\n✅ Server started successfully!")
        print(f"🌐 Dashboard URL: {url}")
        print(f"📡 SSE Stream: http://localhost:{PORT}/stream")
        print(f"📁 Serving from: {os.getcwd()}")
        print(f"\n📖 Features:")
        print(f"   • Real-time updates (2-second polling)")
        print(f"   • No WebSocket dependencies needed")
        print(f"   • Auto-detects new scans")
        print(f"   • Live charts and visualizations")
        print(f"\n🔄 Make sure monitor is running:")
        print(f"   python demo_monitor.py --interval 15")
        print("=" * 70)
        print(f"\n⏳ Server running... Press Ctrl+C to stop\n")

        try:
            # Try to open browser
            import webbrowser
            webbrowser.open(url)
            print("🌐 Opening dashboard in your browser...")
        except:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped. Goodbye!")


if __name__ == "__main__":
    main()
