from scapy.all import sniff

def print_it_please(packet):
    print(f"Un petit pong qui revient de 10.2.1.54 : {packet}")

sniff(filter="icmp and src host 10.2.1.54", prn=print_it_please, count=1)

