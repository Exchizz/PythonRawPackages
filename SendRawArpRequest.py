#!/usr/bin/env python
from socket import socket, AF_PACKET, SOCK_RAW, inet_aton
from binascii import *
from struct import *

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("wlan0", 0))

htype = "\x00\x01" # Hardware type - Ethernet = 1
ptype = "\x08\x00" # Protocol type -ipv4 = 0800
hlen  = "\x06" # Hardware length - length of MAC = 6
plen  = "\x04" # Protocol lenght in bytes, 4 for ipv4
operation = "\x00\x01" # Operation, 1 = request, 2 = answer
sha = "\x24\x77\x03\x26\xb0\x10" # Sender hardware request (MAC address of sender)
spa = inet_aton("172.16.0.10") # Sender protocol address = ip address of sender
tha = "\x00\x00\x00\x00\x00\x00" # target hardware address (ignored in request)
tpa = inet_aton('172.16.0.15') # Target protocol address

src_addr = "\x24\x77\x03\x26\xb0\x10"
dst_addr = "\xff\xff\xff\xff\xff\xff"
payload = htype + ptype + hlen + plen + operation + sha + spa + tha + tpa
ethertype = "\x08\x06"

checksum = '%08X' % (crc32(dst_addr+src_addr+ethertype+payload) & 0xffffffff)
print checksum
s.send(dst_addr+src_addr+ethertype+payload+checksum)
