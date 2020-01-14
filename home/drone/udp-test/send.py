#!/usr/bin/env python

import socket
import time
import datetime


UDP_IP = "192.168.192.103"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "Sending message"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

while True:
    now = datetime.datetime.now()
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE + now.strftime("%c"), (UDP_IP, UDP_PORT))
    time.sleep(0.5)