from scapy.all import *

# Construire la requête DNS
def dns_query(domain):
    # Créer une trame Ethernet (source MAC et destination MAC)
    ether = Ether(dst="ca:01:16:e1:00:00", src="08:00:27:52:78:05")
    
    # Créer une couche IP (adresse source et destination)
    ip = IP(src="10.2.1.54", dst="8.8.8.8")  # DNS Google Public (8.8.8.8)
    
    # Créer une couche UDP (port source et destination)
    udp = UDP(sport=RandShort(), dport=53)  # Port 53 est le port DNS
    
    # Créer une requête DNS pour le domaine
    dns = DNS(rd=1, qd=DNSQR(qname=domain, qtype="A"))  # Requête A pour le domaine
    
    # Combiner toutes les couches
    packet = ether / ip / udp / dns
    
    # Envoyer la requête en utilisant srp() et récupérer la réponse
    response = srp(packet, timeout=2, verbose=1)[0]  # timeout de 2 secondes
    
    # Afficher la réponse
    for _, rcv_pkt in response:
        if rcv_pkt.haslayer(DNSRR):  # Vérifier s'il y a une réponse DNS
            print(f"Réponse DNS reçue pour {domain}: {rcv_pkt[DNSRR].rdata}")
        else:
            print("Aucune réponse DNS reçue.")

if __name__ == "__main__":
    domain = "www.google.com"  # Domaine pour la requête DNS
    dns_query(domain)

