# on importe la lib scapy
from scapy.all import *

# on craft un ping : c'est de l'ICMP
# type 8 pour ICMP echo request (le ping)
ping = ICMP(type=8)

# on craft un paquet : IP src et IP dst
# 10.3.223.123 : l'IP de mon PC chez moi
# 10.3.0.1 : l'IP de ma box chez moi, ma passerelle
packet = IP(src="10.3.223.123", dst="10.3.0.1")

# on craft une trame : MAC src et MAC dst
# d4:6d:6d:00:15:3b : la MAC de mon PC chez moi
# 78:94:b4:de:fd:c4 : la MAC de ma box chez moi, ma passerelle
frame = Ether(src="10:ff:e0:07:c6:10", dst="00:09:0f:09:00:26")

# on emboîte le tout avec le caractère /
final_frame = frame/packet/ping

# srp() c'est pour send & receive
# fonction à utiliser quand on envoie un truc et qu'on attend une réponse
# ici, on envoie un ping et on attend un pong
answers, unanswered_packets = srp(final_frame, timeout=10)

# on a récupéré les pongs dans answers
# et les pings qui n'ont jamais eu de réponses sont dans unanswered_packets
print(f"Pong reçu : {answers[0]}")

