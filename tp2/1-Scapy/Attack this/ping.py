from scapy.all import *
ans, unans = srp(IP(dst="1.1.1.1")/ICMP(), timeout=10)
print(ans)

