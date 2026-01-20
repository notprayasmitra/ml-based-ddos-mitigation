# Main proxy server for basic MVP
# Implements threshold-based blocking and logging

import socketserver, threading, time, os

THRESHOLD = 100  # requests per minute
LOG_DIR = '../logs/'
LOG_FILE = os.path.join(LOG_DIR, 'traffic.log')
ip_counts = {}
lock = threading.Lock()

class ProxyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ip = self.client_address[0]
        now = int(time.time())
        with lock:
            ip_counts.setdefault(ip, []).append(now)
            # Clean up old timestamps
            ip_counts[ip] = [t for t in ip_counts[ip] if now - t < 60]
            count = len(ip_counts[ip])
        if count > THRESHOLD:
            log_event(f"Blocked {ip} at {now}")
            return
        data = self.request.recv(1024)
        log_event(f"{ip} {now} {len(data)} bytes")
        # ...forward to backend if needed...

def log_event(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(msg + '\n')

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("0.0.0.0", 8080), ProxyHandler)
    print("Proxy server running on port 8080...")
    server.serve_forever()
