#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.weasner.com/etx/autostar/as_testing.html
# Socket Server functions
# Send Serial function using queues so only one process
# send messages to the Telescope at the time
from Queue import Queue
import struct
import socket
import threading
import select
import sys
import serial.tools.list_ports;
import serial
from MeadeDictionary import *
from TelescopeSerialChannelClass import *
from coords import *
from time import sleep
import datetime as dt

# q_tx_SerialMsg=Queue()
# q_rx_SerialMsg=Queue()
lock = threading.Lock()
q_updateCoordsStellarium=Queue()

def SerialMsgToQueue(msg,arg=None):
    ''' SerialMsgToQueue(msg,arg=None)
     MsgSerialToQueue process will extract the message
     from q_tx_SerialMsg queue  and send it via Serial Channel
     and will return the response given by the Telescope

    '''
    q_tx_SerialMsg.put((msg,arg))
    PrintMsg("SERVER: SerialMsgToQueue - Tx = "+str(msg)+" "+str(arg))
    
    # MsgSerialToTelescope will send data to Telescope and wait in the queue for replay.
    # Then it will put the response into the q_rx_SerialMsg queue
    rx=q_rx_SerialMsg.get()

    PrintMsg("SERVER: SerialMsgToQueue - Rx = "+str(rx))
    PrintMsg("SERVER: SerialMsgToQueue - arg = "+str(arg))
    return(rx)

# Print function using queues so I can from threads in sequence
q_print=Queue()

def PrintMsg(msg):
    q_print.put(msg)
    
def printToQueue():
    while True:
        item = q_print.get()
        print item
  
#----------------------------------------------------------------------------------------------------
# Define low level socket functions to manage length of the mesagge tx or rx
# from user interface to the socket server the message has a header indicating the size
# of the message
# Stellarium has a different message but also has a header of two byted with the length of the
# message
#----------------------------------------------------------------------------------------------------

# Add the length of the message at the begining of each mesage to TX
def tx_tcp_msg(sock, msg):
    # Prefix each message with a 2-byte length (\x00\x12)(big-endian, unsigned short int(2 bytes)
    msg = struct.pack('<H', len(msg)+2) + msg
    PrintMsg("SERVER:tx_tcp_msg: Add msg length and send msg to Client ->"+str(msg))
    #PrintMsg("Msg Length = "+str(len(msg)))
    # Check error sending here: If Telescope Client is down SocketServer will
    # only only one message from Stellarium
    sock.sendall(msg)
    
# Send TCP message to Stellarium via socket   
def tx_tcp_msg_stell(sock, s_msg):
    LENGTH=24
    msg=struct.pack('<hHQIii',LENGTH,s_msg[0],s_msg[1],s_msg[2],s_msg[3],s_msg[4])
    sock.sendall(msg)
    sock.sendall(msg)
    sock.sendall(msg)
    
# Read the first message to extract the length of the message to RX
def rx_tcp_msg(sock):
    # Read message length (two bytes) and unpack it into an integer
    raw_msglen = recvall(sock,2)
    
    if not raw_msglen:
        return None
    msglen = struct.unpack('<H', raw_msglen)[0]-2
    
    PrintMsg("SERVER: rx_tcp_msg: rx_msg_length "+ str(msglen))
    # Read the message data
    return recvall(sock, msglen)

    
    
def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''  # CP...I think this initialize "data" a a binary variable
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data



#----------------------------------------------------------------------------------------------------
#  Define functions to be called once a command is received from the Client machine
#  Commands are sent via serial channel to the Telescope attached to the remote machine(Raspberri PI)
#-----------------------------------------------------------------------------------------------------

def move_up(cmd_arg):
    PrintMsg("Up")
    SerialMsgToQueue(TEL_CMD['EXE_MOVE_NORTH'])

def stop_up(cmd_arg):
    PrintMsg("Stop_Up")
    SerialMsgToQueue(TEL_CMD['EXE_STOP_MOVE_NORTH'])

def move_down(cmd_arg):
    PrintMsg("Down")
    SerialMsgToQueue(TEL_CMD['EXE_MOVE_SOUTH'])

def stop_down(cmd_arg):
    PrintMsg("Stop_Down")
    SerialMsgToQueue(TEL_CMD['EXE_STOP_MOVE_SOUTH'])

def move_left(cmd_arg):
    PrintMsg("Left")
    SerialMsgToQueue(TEL_CMD['EXE_MOVE_EAST'])

def stop_left(cmd_arg):
    PrintMsg("Stop_Left")
    SerialMsgToQueue(TEL_CMD['EXE_STOP_MOVE_EAST'])

def move_right(cmd_arg):
    PrintMsg("Right")
    SerialMsgToQueue(TEL_CMD['EXE_MOVE_WEST'])

def stop_right(cmd_arg):
    PrintMsg("Stop_Right")
    SerialMsgToQueue(TEL_CMD['EXE_STOP_MOVE_WEST'])

def speed1(cmd_arg):
    PrintMsg("Speed1")
    SerialMsgToQueue(TEL_CMD['SET_SLEW_GUIDE'])

def speed2(cmd_arg):
    PrintMsg("Speed2")
    SerialMsgToQueue(TEL_CMD['SET_SLEW_CENTER'])

def speed3(cmd_arg):
    PrintMsg("Speed3")
    SerialMsgToQueue(TEL_CMD['SET_SLEW_FIND'])

def speed4(cmd_arg):
    PrintMsg("Speed4")
    SerialMsgToQueue(TEL_CMD['SET_SLEW_FAST'])
def setTelescopeDate(cmd_arg):
    PrintMsg("SetDate="+'SET_HANDBOX_DATE '+cmd_arg+"#")
    s=SerialMsgToQueue(TEL_CMD['SET_HANDBOX_DATE'],cmd_arg)
    PrintMsg("SERVER:setTelescopeDate: Rx = "+str(s))

def setLocalTime(cmd_arg):
    PrintMsg('SET_LOCAL_TIME '+cmd_arg+"#")
    ack = SerialMsgToQueue(TEL_CMD['SET_LOCAL_TIME'],cmd_arg)
    if ack != str(1):
        PrintMsg("SERVER: setLocalTime - Error - Cannot set local time. ack =  "+str(ack))

def stopGoTo(cmd_arg):
    PrintMsg("Stop GO To")
    SerialMsgToQueue(TEL_CMD['EXE_STOP_GOTO'])
    
def park(cmd_arg):
    PrintMsg("Park")
    SerialMsgToQueue(TEL_CMD['EXE_PARK'])

def telSleep(cmd_arg):
    PrintMsg("Sleep...")    
    SerialMsgToQueue(TEL_CMD['EXE_SLEEP'])
    
def wakeup(cmd_arg):
    PrintMsg("WakeUp")    
    SerialMsgToQueue(TEL_CMD['EXE_WAKEUP'])  

def alignTelescope(cmd_arg):
    PrintMsg("AlignTelescope")
    reply=SerialMsgToQueue(TEL_CMD['START_AUTO_ALIGNMENT'])
    return(reply)
    
def getTelTimeDate(cmd_arg):
    PrintMsg('ASK_LOCAL_TIME_24')   
    s1=SerialMsgToQueue(TEL_CMD['ASK_LOCAL_TIME_24'])
    PrintMsg("s1= "+str(s1))
    PrintMsg('ASK_CALENDAR_DATE'+"#")   
    s2=SerialMsgToQueue(TEL_CMD['ASK_CALENDAR_DATE'])
    PrintMsg("s2= "+str(s2))
    reply=str(s1)+"%"+str(s2)
    return reply
def getObjRa(cmd_arg):
    # receive this: HH:MM:SS#
    PrintMsg("getObjRA")  
    RA=SerialMsgToQueue(TEL_CMD['ASK_OBJ_RA'])
    PrintMsg("Serial return RA = HH:MM:SS# = "+str(RA))
    return RA
def getTelRa(cmd_arg):
    # receive this: HH:MM:SS#
    PrintMsg("getTelRA")  
    RA=SerialMsgToQueue(TEL_CMD['ASK_TEL_RA'])
    PrintMsg("Serial return RA = HH:MM:SS# = "+str(RA))
    return RA    
    
def getObjDec(cmd_arg):
    # receive this: sDD*MMSS#
    PrintMsg("getObjDEC")  
    DEC=SerialMsgToQueue(TEL_CMD['ASK_OBJ_DEC'])
    PrintMsg("Serial return: sDD*MM:SS# = "+str(DEC))
    return DEC

def getTelDec(cmd_arg):
    # receive this: sDD*MMSS#
    PrintMsg("getTelDEC")  
    DEC=SerialMsgToQueue(TEL_CMD['ASK_TEL_DEC'])
    PrintMsg("Serial return: sDD*MM:SS# = "+str(DEC))
    return DEC   
    
def getTelAlignment(cmd_arg): # This command does not work yet
    PrintMsg("getTelAlignment = "+"0x6")
    ALIGN=SerialMsgToQueue(TEL_CMD['ASK_ALIGNMENT']) #ASK_ALIGNMENT
    PrintMsg("Alignment = "+ALIGN)
    return ALIGN

def getTelSiteName(cmd_arg):
    PrintMsg("getTelSiteName")
    # Reads until receive a End of serial command (#) Length of Site Name could be eny number of characters
    SITENAME=SerialMsgToQueue(TEL_CMD['ASK_SITE_NAME'])
    return SITENAME

def getTelAltitud(cmd_arg):
    # Returns: sDD*MM# or sDD*MMSS#
    PrintMsg("getTelAltitud")
    ALT=SerialMsgToQueue(TEL_CMD['ASK_TEL_ALT'])
    return ALT

def getTelAzimuth(cmd_arg):
    # Returns: DDD*MM#T or DDD*MMSS#
    PrintMsg("getTelAzimuth")
    AZM=SerialMsgToQueue(TEL_CMD['ASK_TEL_AZ'])
    return AZM
    

def stellariumGoTo (cmd_arg):

    # arg = '12:00:00'+"|"+'-14:00:00'
    ra=cmd_arg[:cmd_arg.index("|")]
    dec=cmd_arg[cmd_arg.index("|")+1:]
    
    PrintMsg("SERVER: StellariumGoTo - tx Serial = "+str(ra)+" "+str(dec))

    ret_ra=SerialMsgToQueue(TEL_CMD['SET_OBJ_RA'],ra)
    ret_dec=SerialMsgToQueue(TEL_CMD['SET_OBJ_DECLINATION'],dec)
    PrintMsg("SERVER:stellariumGoTo - Ra and Dec response = "+str(ret_ra)+","+str(ret_dec))
    
    if ret_ra==0:
        PrintMsg("SERVER:stellariumGoTo - GoTo RA Error")

    if ret_dec==0:
        PrintMsg("SERVER:stellariumGoTo - GoTo DEC Error")

    #Returns:
    #0 Slew is Possible
    #1<string># Object Below Horizon w/string message
    #2<string># Object Below Higher w/string message
    if ret_ra and ret_dec:
        PrintMsg("SERVER:stellariumGoTo - Tx Serial - > Goto to Telsecope ")
        ret = SerialMsgToQueue(TEL_CMD['EXE_GOTO'])
        PrintMsg("SERVER: StellariumGoTo Return Goto command = "+str(ret))
    else:
        PrintMsg("SERVER:stellariumGoTo - Tx Serial - > GOTO ERROR SENDING RA or DEC to Telescope ")
        ret = '0'

    # check if object is below horizon  ret = 1,2<string>#
    if ret[0] != '0':
        # ret=SerialMsgToQueue(TEL_CMD['ADDITIONAL_STR'])
        PrintMsg("SERVER:stellariumGoTo - Goto Response = Object Below Horizon")
        # here i should send some message to the user interface
        # PrintMsg("SERVER:stellariumGoTo - Goto Response = "+str(ret))
    else:
        # return to Stellarium 
        PrintMsg("SERVER: StellariumGoTo - Goto Response = "+str(ret))
    return 'STELLARIUM' # send a string to let know the socket it was a goto stellatium command

def getSiteLatitude(cmd_arg): 
    PrintMsg("getSiteLatitude = "+"ASK_SITE_LAT")
    S_LAT=SerialMsgToQueue(TEL_CMD['ASK_SITE_LAT']) #ASK_SITE_LAT
    PrintMsg("Site Latitude = "+S_LAT)
    return S_LAT    
def getSiteLongitude(cmd_arg):  
    PrintMsg("getSiteLongitude = "+"ASK_SITE_LONG")
    S_LONG=SerialMsgToQueue(TEL_CMD['ASK_SITE_LONG']) #ASK_SITE_LONG
    PrintMsg("Site Longitude = "+S_LONG)
    return S_LONG

# options dictionary is used to decode the received message from User Interface or Stellarium
options = {
    "Up": move_up,
    "Stop_Up": stop_up,
    "Down": move_down,
    "Stop_Down": stop_down,
    "Left": move_left,
    "Stop_Left": stop_left,
    "Right": move_right,
    "Stop_Right": stop_right,
    "Speed1": speed1,
    "Speed2": speed2,
    "Speed3": speed3,
    "Speed4": speed4,
    "TelescopeDate": setTelescopeDate,
    "LocalTime": setLocalTime,
    "StopGoTo": stopGoTo,
    "Park": park,
    "TelSleep": telSleep,
    "AlignTelescope": alignTelescope,
    "GetTelTimeDate": getTelTimeDate,
    "GetTelRA": getTelRa,
    "GetTelDEC": getTelDec,
    "GetObjRA": getObjRa,
    "GetObjDEC": getObjDec,
    "GetTelAlignment": getTelAlignment,
    "GetTelSiteName": getTelSiteName,
    "GetTelAltitud": getTelAltitud,
    "GetTelAzimuth": getTelAzimuth,
    "GetSiteLatitude": getSiteLatitude,
    "GetSiteLongitude": getSiteLongitude,
    "Stellarium": stellariumGoTo
}

# every time a tcp connection is requested to the server a new thread is created and
# the function below is called
# the user interface and stellarium trigger the tcp connections

def listenToClient(skt,addr):
    t = threading.currentThread()
    PrintMsg('SERVER: '+ str(t))
    UpdateStellariumCoords = False
    PrintMsg('SERVER: listenToClient - NEW Connection from ' + str(addr))
    is_readable = [skt]
    is_writable = []
    is_error = []
    
    while True:
        UpdateCoords = False

        # UpdateStellariumCoords = False
        # Validate if there is something to read from the socket but do not wait more than a 1 second


        try:
            # use queue.get(False) = queue.get_nowait > get without blocking to check if there is something in the queue
            UpdateCoords = q_updateCoordsStellarium.get_nowait()
            # if there is something in the queue the return value is True or False
            PrintMsg("SERVER: "+str(addr[1])+"->listenToClient - UpdateCoords = "+str(UpdateCoords))
        except Exception as e:
            # If there is nothing in the queue the return value is not provided so UpdateCoords is not changed
            PrintMsg("SERVER: "+str(addr[1])+"->listenToClient - UpdateCoords = "+str(UpdateCoords))
            
        if UpdateCoords:
            UpdateStellariumCoords = True

        # Is there something to read in socket?
        r, w, e = select.select(is_readable, is_writable, is_error,0.0)
        PrintMsg("Outside update stellarium r = "+ str(r))

        # if there is nothing to read from Stellarium and UpdateStellariumCoords flag was activated then enter the loop
        # to send coords to Stellarium
        # but if there is something to read exit the loop and go to check what command was sent by
        # stellatium
        while (not r and UpdateStellariumCoords):
            r, w, e = select.select(is_readable, is_writable, is_error,0.0)
            PrintMsg("Inside update stellarium r = " + str(r))
            # Send data to Stellarium every second
            sleep(1)
            PrintMsg("SERVER: "+str(addr[1])+"->listenToClient - Entering UpdateStellarium loop")
            # Request object coordinates to Telescope via Serial Channel
            #lock.acquire()
            ra=getTelRa('Stellarium')  # getTelRa does not use the argument stellarium ??
            #lock.release()
            if ra=="":
                PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - TelRA: ERROR")
                #lock.release()
                break
            dec=getTelDec('Stellarium') # getTelDec does not use the argument stellarium ??
            if dec=="":
                PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - TelDEC: ERROR")
                #lock.release()
                break
            #lock.release()

            PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - TelRA  = "+str(ra))
            PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - TelDEC = "+str(dec))
            
            ra_h  = float(ra[:2])+float(ra[3:5])/60+float(ra[6:8])/3600
            dec_d = float(dec[:3])+float(dec[4:6])/60+float(dec[7:9])/3600
            ra_stl = int(ra_h*(2147483648/12.0))
            dec_stl = int(dec_d*(1073741824/90.0))
            
            # Time is not used in Stellarium protocol so, I took machine time instead of Telescope Time
            stl_time=int((dt.datetime.utcnow() - dt.datetime(1970, 1, 1)).total_seconds() )

            PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - TelTime = "+str(stl_time))
            x = dt.datetime.now()
            PrintMsg(x.strftime("%X"))

            TYPE = 0
            STATUS = 0
            PrintMsg("SERVER: "+str(addr[1])+"->TelPosToStellarium - Sending cmd = "+str(TYPE)+","+ str(stl_time)+","+str(ra_stl)+","+str(dec_stl)+","+str(STATUS))
            stellarium_cmd = (TYPE, stl_time,ra_stl, dec_stl,STATUS)
            #----------------------------------------------------------------------------------------
            #    SENT COORDINATE UPDATE TO STELLARIUM
            tx_tcp_msg_stell(skt, stellarium_cmd)
            #----------------------------------------------------------------------------------------
    

        #----------------------------------------------------------------------------------------
        # Wait till something is received from socket.
        # Read command from Client via Socket        
        #----------------------------------------------------------------------------------------
        cmd = rx_tcp_msg(skt)
        #----------------------------------------------------------------------------------------
        PrintMsg("SERVER: "+str(addr[1])+"-> listenToClient - TCP cmd received = "+str(cmd))



        #-----------------------------------------------------------------------------------
        # Check if command came from Stellarium
        # If first byte = \x00\x00 the command came from Stellarium 
        #-----------------------------------------------------------------------------------
        if struct.unpack('h',cmd[0:2])[0]==0:
            stellarium_cmd=struct.unpack('<HQIi', cmd)
            PrintMsg("SERVER: "+str(addr[1])+"-> listenToClient - Rx from Stellarium = "+str(stellarium_cmd))
            x=stellarium_cmd
            ra=hour_min_sec(x[2]*12.0/2147483648)
            dec=grad_min_sec(x[3]*90.0/1073741824)
            ra_str='%02d:%02d:%02d' %ra
            dec_str='%0.2d*%02d:%02d' %dec
            cmd="Stellarium%"+ra_str+"|"+dec_str

            PrintMsg("SERVER: "+str(addr[1])+"-> listenToClient: Stellarium tracking ACTIVATED: "+cmd)
            # Activate Telescope location visualization in Stellarium
            UpdateStellariumCoords = True
            q_updateCoordsStellarium.put(True)
        else:
            # q_updateCoordsStellarium.put(False)
            UpdateStellariumCoords = False
        #----------------------------------------------------------------------------------
        # After finishing reading data from client, server start analyzing what command was received
        # Determine what command was received using options dictionary

        # From data received, Server separates command from the argument:
        # % Is a separator between the command and the argument if there is any
        #---------  Command format below   -------------
        #               cmd%arg|
        #-----------------------------------------------

        #lock.acquire()
        cmd_cmd=cmd[:cmd.index("%")]
        cmd_arg=cmd[cmd.index("%")+1:]
        #lock.release()
        # Send the command received via socket to the Telescope via serial channel
        # Call the command (cmd_cmd) and pass an agrument (cmd_arg) if it is required
        reply=options[cmd_cmd](cmd_arg)
        # reply has data received from telescope via serial channel
        # Client always wait for reply msg except if the message was for stellarium

        if reply != None:
            tx_tcp_msg(skt,reply)
        else:
            # If command does not return data function sent msg = Done
            PrintMsg("SERVER: "+str(addr[1])+"-> listenToClient - Sending to client: Done => No response from Telescope")
            # if message was related to stellarium do not send a tcp replay
            if reply != "STELLARIUM":
                tx_tcp_msg(skt,"Done")

        # Close the socket after send back message received from telescope
        # If original message was from stellarium socket is not closed and is used to update
        # stellarium with the coordinates received from the telescope.
        if  not UpdateStellariumCoords:
            # Break to jump out of the loop and close the socket
            break

    # Close socket after reply
    PrintMsg("SERVER: "+str(addr[1])+"->listenToClient - Close Socket")
    skt.close()
    PrintMsg("SERVER: Closing " + str(t.getName()))
    return # force closing the thread ??
