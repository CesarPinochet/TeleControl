# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 08:18:12 2018

@author: d351157
"""
#
import socket
import sys
import struct

# pip install pyserial  => serial.tools...
import serial.tools.list_ports;

import serial
import re
from  time import sleep
from Queue import Queue

q_tx_SerialMsg=Queue()
q_rx_SerialMsg=Queue()

class TelescopeSerialChannel():
    #comp = serial.tools.list_ports.comports()
    #ports = [comport.device for comport in serial.tools.list_ports.comports()]
    #ports_name = [comport.name for comport in serial.tools.list_ports.comports()]
    #ports_decription = [comport.description for comport in serial.tools.list_ports.comports()]
    
    def initialize(self):
        ini=False
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            #if 'USB and Serial' in p.description:
            search_result = re.search(r'USB.*Serial', p.description, re.M | re.I)
            if search_result <> None :
                print p.description, p.device
                print str(p.vid)+str(p.pid)
                if str(p.vid)+str(p.pid) == '13678200':
                    Port=p.device
                    ini=True   # Finds USB to Serial port
        if not ini: 
            return (ini) # Did not find USB to Serial port
        try:
            self.ser = serial.Serial(port=Port, baudrate=9600, bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=5,rtscts=0)
        except IOError as e:
            ini=False  # Error opening the serial port
            print e
        if ini: 
            self.ser.isOpen() # If there was no error open the serial chanel
        return (ini)
    
    def send_serial_msg(self,code,arg=None):
        # Code is a tuple (TelCmd,n_Char to rx) and arg = telCmd Argument like a date 07/05/18
        # n_Char to Receive can be a # indicating read until a  # arrives
        self.ser.flushInput()
        self.ser.flushOutput()
        if arg==None:
            msg = code[0]+'#'
        else:
            msg = code[0]+arg+'#'
            
        rx_length=code[1]
        self.ser.timeout = 5
        self.ser.write(msg)
        
        if rx_length != '#':
            if rx_length == 0:
                return None
            serial_reply = self.ser.read(rx_length)
        else:
            # Read all characters in rx buffer 
            # First read one character, this ensure it waits till there is data to read
            # then wait for the buffer to be full and read all buffer content
            serial_reply=self.ser.read(1)
            sleep(0.1)
            serial_reply=serial_reply+self.ser.read(self.ser.inWaiting())
        return(serial_reply)
        
#
