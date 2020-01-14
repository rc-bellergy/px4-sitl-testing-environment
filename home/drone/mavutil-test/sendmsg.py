#!/usr/bin/env python

# mavutil testing
# Sending Messages
# created by: rc@bellergy.com

import pymavlink.mavutil as mavutil
import time

def print_all_msg():
    loop = 100
    while loop > 0:
        msg = connection.recv_msg()
        if msg is not None:
            print(msg)
            loop = loop -1

drone_endpoint = "udp:127.0.0.1:14560"
connection = mavutil.mavlink_connection(drone_endpoint)

# Send 
while True:
    test = connection.mav.system_time_send(6530224000, 100)
    print(test)
    time.sleep(1)

