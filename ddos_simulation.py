import random
from scapy.all import IP, TCP, send

def send_tcp_packets(dst_ip="127.0.0.1", dst_port=12345, count=10):
    for i in range(count):
        packet = IP(dst=dst_ip)/TCP(dport=dst_port, sport=1024+i)
        send(packet, verbose=False)
        print(f"Sent TCP packet {i+1} to {dst_ip}:{dst_port}")

def main():
    threshold = random.choice([10, 20, 30])
    print("=== DDoS Simulation ===")
    try:
        count = int(input("How many packets do you want to send? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    send_tcp_packets(count=count)

    print(f"\n[Server] DDoS threshold is {threshold} packets.")
    if count >= threshold:
        print("[Server] DDoS detected! Too many packets sent.")
    else:
        print("[Server] No DDoS detected. All is normal.")

if __name__ == "__main__":
    main()