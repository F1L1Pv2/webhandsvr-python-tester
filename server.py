#udp server for receiving data from the client on port 6969 
import socket
import time
import threading
import struct


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 8000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

def receive():
    while True:
        data, address = sock.recvfrom(4096)
        #b'/imuquat\x00\x00\x00\x00,ssss\x00\x00\x00 0.97\x00\x00\x00 0.00\x00\x00\x00 0.02\x00\x00\x00-0.23\x00\x00\x00'
        

        print(data.decode('utf-8'))

            


            


if __name__ == "__main__":
    t1 = threading.Thread(target=receive)
    t1.start()