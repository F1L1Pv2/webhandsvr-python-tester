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
# server_address = ('localhost', 6969)

# Initialize the OpenVR system
# openvr.init(openvr.VRApplication_Scene)
openvr.init(openvr.VRApplication_Other)

#PosX1|PosY1|PosZ1|RotX1|RotY1|RotZ1|PosX2|PosY2|PosZ2|RotX2|RotY2|RotZ2|A|B|X|Y|Joy1X|Joy1Y|Joy2X|Joy2Y|Trig1|Trig2|Grip1|Grip2|AppMenu1|AppMenu2|Joy1Click|Joy2Click

pos1=[0,0,0]
pos2=[0,0,0]
rot1=[1,0,0,0]
rot2=[1,0,0,0]

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

angle = 0

while True:

        # Get the HMD pose
    # hmd_pose = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, 1)
    hmd_pose = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseRawAndUncalibrated, 0, 1)
    # hmd_pose2 = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseOrigin, 0, 1)

    # Extract the position of the HMD
    hmd_position = hmd_pose[0].mDeviceToAbsoluteTracking
    # hmd_position2 = hmd_pose2[0].mDeviceToAbsoluteTracking

    # print(hmd_position2)

    # Convert the tuple of rows to a numpy array
    hmd_matrix = np.array([hmd_position[0], hmd_position[1], hmd_position[2]])

    # Extract the position
    hmd_position = hmd_matrix[:, 3]
    print(hmd_position)
    
    angle += 0.01

    newX= math.cos(math.radians(angle)) * 0.2
    newZ= math.sin(math.radians(angle)) * 0.2

    posX1 = hmd_position[0] + newX
    posY1 = hmd_position[1] 
    posZ1 = hmd_position[2] + newZ

    pos1=[posX1,posY1,posZ1]


    message = f"{'|'.join(str(x) for x in pos1)}|{'|'.join(str(x) for x in rot1)}|{'|'.join(str(x) for x in pos2)}|{'|'.join(str(x) for x in rot2)}|{A}|{B}|{X}|{Y}|{Joy1X}|{Joy1Y}|{Joy2X}|{Joy2Y}|{Trig1}|{Trig2}|{Grip1}|{Grip2}|{AppMenu1}|{AppMenu2}|{Joy1Click}|{Joy2Click}|{System1}|{System2}"
    print(message)

    
    # Send data
    try:
        sent = sock.sendto(message.encode(), server_address)
        #rotX1 += 0.01
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        break


# sock.close()
# openvr.shutdown()