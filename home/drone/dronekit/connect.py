#!/usr/bin/env python

from dronekit import connect
vehicle = connect('127.0.0.1:14560', wait_ready=True)
print("Mode: %s" % vehicle.mode.name)