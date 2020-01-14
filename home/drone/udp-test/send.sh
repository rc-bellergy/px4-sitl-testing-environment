#!/bin/bash

while [ : ]
do
    echo "The time is $(date)" > /dev/udp/192.168.192.103/3000
    sleep 1
done