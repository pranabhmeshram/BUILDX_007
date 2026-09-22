import http.server
import socketserver
import webbrowser
import os
import sys

# Ensure UTF-8 output encoding for VS Code Windows Terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class VSCodeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def start_server():
    global PORT
    for try_port in [8080, 8081, 8082, 5500, 3000]:
        try:
            with socketserver.TCPServer(("", try_port), VSCodeHandler) as httpd:
                PORT = try_port
                url = f"http://localhost:{PORT}"
                print("============================================================")
                print(f"[RAKSHA-SETU 360] Web Server Active for VS Code")
                print(f"Website URL: {url}")
                print("============================================================")
                try:
                    webbrowser.open(url)
                except Exception:
                    pass
                httpd.serve_forever()
                break
        except OSError:
            continue

if __name__ == "__main__":
    start_server()
