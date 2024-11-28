from scapy.all import sniff

def print_it_please(packet):
    packet_source_ip = packet['IP'].src
    pong = packet['ICMP']
    print(f"Un petit pong qui revient de {packet_source_ip} : {pong}")

sniff(filter="icmp and src host 10.2.1.54", prn=print_it_please, count=1)

