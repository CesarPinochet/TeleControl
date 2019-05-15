#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
# http://www.weasner.com/etx/autostar/as_testing.html

from TelescopeSerialChannelClass import *
# from coords import *
from SocketServerFunctions import *

port_error=0

def MsgSerialToTelescope():
    ''' MsgSerialToTelescope() - Send commands via serial port to Telescope and send back Telescope reply if there is any'''
    while True:
        msg, arg = q_tx_SerialMsg.get()
        #item = q_tx_SerialMsg.get()
        # The queue should have msg + argument
        #SerialResponse=xSerial.send_serial_msg(item[0],item[1])
        SerialResponse = xSerial.send_serial_msg(msg, arg)
        q_rx_SerialMsg.put(SerialResponse)


# Create one thread to allow multiple threads print in sequence
th_qPrint = threading.Thread(target = printToQueue)
th_qPrint.start()

# Create one thread to manage the serial communication with the Telescope
th_qSerial = threading.Thread(target = MsgSerialToTelescope)
th_qSerial.start()

# Create a thread to request Telescope ra/dec and report
# back to Stellarium each 10 second.
#th_TelToStell = threading.Thread(target = TelPosToStellarium)           
#th_TelToStell.start()
         
"""
#-------------------------------------------------------------------------
# Initialize serial port COM x connected to an USB Serial converter
# Set it for 9600 bits per second, 8 data bits, Parity:None, StopBits: !
# Flow Control: None
#-------------------------------------------------------------------------
"""
PrintMsg("STARTING THE SERVER")
PrintMsg("Ports Available")
PrintMsg([comport.device for comport in serial.tools.list_ports.comports()])
#print [port for port in serial.tools.list_ports.comports() if port[2] != 'n/a']



# Create a TCP/IP socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PrintMsg("SERVER: Socket successfully created")
    # In this case, the address is localhost, referring to the current server, and the port number is 10000.
    # Bind the socket to the port
    # Never bind a socket to localhost unless all modules are in the same machine
    server_address = ('192.168.11.252', 10000)

except socket.error as err:
    print "SERVER: socket creation failed with error %s" %(err)
finally:
    PrintMsg("SERVER: socket starting up on " + str(server_address[0])+ " port " + str(server_address[1]))

# Then bind() is used to associate the socket with the server address.
sock.bind(server_address)
# Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
# Listen for incoming connections
sock.listen(1)
PrintMsg("SERVER: SOCKET Initiated - Server socket is listening")


# Opening serial channel to comunicate with Telescope
PrintMsg("SERVER: Opening Telescope Serial Channel")
xSerial = TelescopeSerialChannel()

if not xSerial.initialize():
    PrintMsg ("SERVER: Error opening Serial Channel")
    quit()

PrintMsg("SERVER: Serial Channel opened successfully")
main_thread = threading.current_thread()
PrintMsg("SERVER: "+str(main_thread))
while True:
    # Wait for a connection
    PrintMsg( 'SERVER: MAIN LOOP - Socket waiting for a connection')
    conn, client_address = sock.accept()
    th = threading.Thread(target = listenToClient,args = (conn,client_address))
    PrintMsg("SERVER: MAIN LOOP - Socket configured"+str(client_address))
    th.daemon = True
    th.start()
    PrintMsg("SERVER: MAIN LOOP - Socket started"+str(client_address))

# Creo nunca pasa por aqui    
PrintMsg("Closing serial Channel")
ser.close()




