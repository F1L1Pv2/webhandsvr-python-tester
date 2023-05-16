#python udp client
import socket
import sys
import json
import time
import openvr
import numpy as np
import math

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 49152)

posX1 = 0
posY1 = 0
posZ1 = 0
rotX1 = 0
rotY1 = 0
rotZ1 = 0
posX2 = 0
posY2 = 0
posZ2 = 0
rotX2 = 0
rotY2 = 0
rotZ2 = 0
A = 0
B = 0
X = 0
Y = 0
Joy1X = 0
Joy1Y = 0
Joy2X = 0
Joy2Y = 0
Trig1 = 0
Trig2 = 0
Grip1 = 0
Grip2 = 0
AppMenu1 = 0
AppMenu2 = 0
Joy1Click = 0
Joy2Click = 0
System1 = 0
System2 = 0


while True:
    message = f"{posX1}|{posY1}|{posZ1}|{rotX1}|{rotY1}|{rotZ1}|{posX2}|{posY2}|{posZ2}|{rotX2}|{rotY2}|{rotZ2}|{A}|{B}|{X}|{Y}|{Joy1X}|{Joy1Y}|{Joy2X}|{Joy2Y}|{Trig1}|{Trig2}|{Grip1}|{Grip2}|{AppMenu1}|{AppMenu2}|{Joy1Click}|{Joy2Click}|{System1}|{System2}"
    
    # Send data
    try:
        sent = sock.sendto(message.encode(), server_address)
        # rotX1 += 0.01
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        break


sock.close()