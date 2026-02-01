#!/usr/bin/env python3
"""
Simple HTTP server to serve the dashboard
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8888

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files and directory listings"""

    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Change to project directory
    os.chdir(Path(__file__).parent)

    Handler = MyHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/dashboard.html"

        print("=" * 70)
        print(f"📊 Vietnamese Stock Monitor Dashboard")
        print("=" * 70)
        print(f"\n✅ Server started successfully!")
        print(f"🌐 Dashboard URL: {url}")
        print(f"📁 Serving from: {os.getcwd()}")
        print(f"\n📖 Instructions:")
        print(f"   1. Open your browser and go to: {url}")
        print(f"   2. Dashboard auto-refreshes every 60 seconds")
        print(f"   3. Press Ctrl+C to stop the server")
        print(f"\n🔄 Tip: Run a scan first if you haven't:")
        print(f"   python demo_monitor.py --scan-once")
        print("=" * 70)
        print()

        # Try to open browser automatically
        try:
            webbrowser.open(url)
            print("🌐 Opening dashboard in your browser...")
        except:
            print("⚠️  Could not open browser automatically. Please open the URL manually.")

        print("\n⏳ Server running... Press Ctrl+C to stop\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped. Goodbye!")

if __name__ == "__main__":
    main()
