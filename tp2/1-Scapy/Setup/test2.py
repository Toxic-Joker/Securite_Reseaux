from scapy.all import *
ans, unans = sr(IP(dst="10.2.1.55")/ICMP(), timeout=10)
#print(ans)
print(f"Pong reçu : {ans[0]}")
