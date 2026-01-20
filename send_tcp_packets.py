from scapy.all import IP, TCP, send

def send_tcp_packets(dst_ip="127.0.0.1", dst_port=12345, count=10):
    for i in range(count):
        packet = IP(dst=dst_ip)/TCP(dport=dst_port, sport=1024+i)
        send(packet, verbose=False)
        print(f"Sent TCP packet {i+1} to {dst_ip}:{dst_port}")

if __name__ == "__main__":
    send_tcp_packets()