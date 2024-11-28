import subprocess

def block_dns_responses(domain):
    """Bloque les réponses DNS pour un domaine spécifique en utilisant iptables."""
    
    # Nous devons convertir le domaine en adresse IP via une requête DNS
    try:
        ip_address = subprocess.check_output(["dig", "+short", domain]).decode().strip()
        if not ip_address:
            print(f"Impossible de résoudre {domain} en adresse IP.")
            return
        
        print(f"Adresse IP résolue pour {domain}: {ip_address}")
        
        # Utilisation d'iptables pour bloquer les réponses DNS à cette IP
        # Bloquer toutes les réponses DNS sur UDP port 53 destinées à l'adresse IP du domaine
        subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-d", ip_address, "-p", "udp", "--dport", "53", "-j", "DROP"])

        print(f"Réponses DNS pour {domain} bloquées.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande dig ou iptables: {e}")

if __name__ == "__main__":
    domain_to_block = "efrei.fr"
    block_dns_responses(domain_to_block)

