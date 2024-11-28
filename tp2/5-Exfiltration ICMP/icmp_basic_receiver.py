#!/usr/bin/env python3
from scapy.all import sniff, ICMP

def process_packet(packet):
    # Vérifie si le paquet est un paquet ICMP et s'il contient des données
    if packet.haslayer(ICMP) and packet[ICMP].type == 0:  # Type 0 pour Echo Reply
        data = bytes(packet[ICMP].payload)
        if data:  # Si des données sont présentes
            print(data.decode('utf-8', errors='ignore'))  # Affiche les données

def main():
    print("Listening for ICMP packets...")
    # Sniffer les paquets ICMP (type 0 et type 8) sur toutes les interfaces
    sniff(filter="icmp", prn=process_packet, store=0)

if __name__ == "__main__":
    main()

