from scapy.all import *

def process_packet(packet):
    # Check if the packet has a TCP layer and is a SYN-ACK packet
    if packet.haslayer(TCP) and packet[TCP].flags == 'SA':
        print("TCP SYN ACK reçu !")
        print(f"- Adresse IP src : {packet[IP].src}")
        print(f"- Adresse IP dst : {packet[IP].dst}")
        print(f"- Port TCP src : {packet[TCP].sport}")
        print(f"- Port TCP dst : {packet[TCP].dport}")
        return True
    return False

def sniff_packets():
    # Sniff packets until the first SYN-ACK is captured
    sniff(filter="tcp", prn=process_packet, stop_filter=process_packet)

if __name__ == "__main__":
    sniff_packets()

