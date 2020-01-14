# PX4 SITL testing environment 

## Login
    ssh-add -K ~/.ssh/drone-dq-dev-server
    ssh drone@drone.dq.hk

---
## Start SITL
    cd ~/px4-firmware
    HEADLESS=1 make px4_sitl jmavsim

## Start Mavlink Router
    mavlink-routerd 127.0.0.1:14550 -e 192.168.192.103:14550 -e 127.0.0.1:14560
