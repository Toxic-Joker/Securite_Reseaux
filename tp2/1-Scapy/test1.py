from scapy.all import *

# par défaut, si on précise rien, avec ICMP(), il fait un ping
# un ping pour rappel c'est un ICMP echo-request (type 8)
ping = ICMP()

# pareil là on met quedal, juste l'IP qu'on veut ping en dst
# on indique pas explicitement la src
packet = IP(dst="1.1.1.1")

# on craft la trame, sans renseigner de niveau Ethernet
# on indique pas quelles adresses MAC mettre en src et dst de la trame
# Scapy va faire le job pour craft une trame fonctionnelle
final_frame = packet/ping

# on send avec sr()
ans, unans = sr(final_frame, timeout=10)

print(f"Pong reçu : {ans[0]}")

