# Simulate traffic to test the proxy
import socket, time

def send_requests(ip, port, count, delay=0.01):
    for _ in range(count):
        try:
            s = socket.socket()
            s.connect((ip, port))
            s.sendall(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")
            s.close()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(delay)

if __name__ == "__main__":
    send_requests("127.0.0.1", 8080, 120)
