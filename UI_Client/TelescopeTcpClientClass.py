# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 08:18:12 2018

@author: Cesar Pinochet
"""

import socket
import sys
import struct

# pip install pyserial  => serial.tools...
#import serial.tools.list_ports

#import serial
#from  time import sleep
#from MeadeDictionary import *

#
class RemoteTcpConnect:
    #def __init__(self,remoteIp=None):
    def __init__(self, remoteIp='localhost'):
        # Socket Client to send commands to Raspberry Pi and control the ETX-90C telescope
        #Create a TCP/IP socket

        self.server_address = (remoteIp, 10000)

#        if remoteIp==None:
#            self.server_address = ('localhost', 10000)
#            #self.server_address = ('192.168.11.7', 10000)
#        else:
#            self.server_address = (remoteIp, 10000)
#            #self.server_address = ('192.168.11.7', 10000)
#
        self.connectionError=False

        try:
            self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Create the socket for listening
        except socket.error as error:
            self.connectionError = True
            print ("Error opening client socket",error)
    
    def connect(self):
        # Connect the socket to the port where the server is listening
        try:
            print ('connecting to IP Address %s, port %s' % self.server_address)
            self.skt.connect(self.server_address)
        except socket.error as error:
            self.connectionError = True
            print ("Error opening client socket",error) 
            self.skt.close()
            self.connectionError = True
            
        if  self.connectionError: # If connection error is true
            return(False)
        else:
            print "Client Socket Rx/Tx successfully created"
            return(True)
        
    def __recvall(self,n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = b''
        while len(data) < n:
            packet = self.skt.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data
        
    def __tx_tcp_msg(self, msg):
        # Prefix each message with a 2-byte length (\x00\x12)(big-endian, unsigned short int(2 bytes)
        msg = struct.pack('<H', len(msg)+2) + msg
        self.skt.sendall(msg)
        
    def __rx_tcp_msg(self):
        # Read message length and unpack it into an integer
        raw_msglen = self.__recvall(2)
        if not raw_msglen:
            return None
        msglen = struct.unpack('<H', raw_msglen)[0]-2
        print("Client rx_msgLength=",msglen)
        # Read the message data
        return self.__recvall(msglen)    
        
    def send_msg(self,msg):
        # Send data from Client to the Server 
        self.__tx_tcp_msg(msg)
        
        # Receive response
        msg_received=self.__rx_tcp_msg()
        print "msg Recived =", msg_received
        self.skt.close()
        if msg_received == "Done":
            return None
        else:      
            return msg_received

