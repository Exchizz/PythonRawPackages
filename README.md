# PythonRawPackages
A collection of scripts to make 'raw' communication across ethernet

SendRawArpRequest.py
 - Sends an ARP request using python. It packs an ARP-request frame as payload into an ethernet frame. This is just an example of how to create an ethernet frames. To run:
   `sudo SendRawArpRequest.py`
    You might wanna change the ip addreses in the code. To see if it works, run wireshark and set filtering to "arp"
    There might be a bug regarding CRC32, haven't testet that yet.


Hopefully some more scripts will start to pop-up at some point in time.
