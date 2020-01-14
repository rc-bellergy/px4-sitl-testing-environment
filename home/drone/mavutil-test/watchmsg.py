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

def print_msg(field):
    while True:
        msg = connection.recv_match(type=field, blocking=True)
        print(msg)
        time.sleep(0.5)

drone_endpoint = "udp:127.0.0.1:14565"
connection = mavutil.mavlink_connection(drone_endpoint)

# Check
# while True:
#     system_time = connection.recv_match(type='SYSTEM_TIME', blocking=True)
#     print(system_time)

# Watch all message
# print_all_msg()

print_msg("HEARTBEAT")
