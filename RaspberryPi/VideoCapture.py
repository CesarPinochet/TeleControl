# -*- coding: utf-8 -*-

# As I understand it, the SC mod intercepts the frame transfer pulses,
# even though the webcam chip is sending pulses to get 5 f/sec the
# connection is broken for as long as you want the exposure this allows
# the more time for the charge on the ccd to accumulate and then the
# software makes the connection and then the next frame pulse in the
# webcam is allowed through to end the exposure.﻿
# Config WebCam for Long Exposure
# set Frames per Second to 5 FPS (1/5th of a second)
# Leave Gamma at zero
# Freeze White Balance.
# Set Auto Off.
# Keep the Gain lower if possible.
# Usually a Gain value of 50% to 75% is sufficient

# How Stack images - link below
# https://github.com/maitek/image_stacking/blob/master/auto_stack.py

# CP: The only way to get clear images with the modified webcam is
# the long exposure mode. The normal mode forces FPS = 30 and this
# generates blurry images. Images are clear below 20 FPS
#
# The long exposure mode is triggered with RTS in High (True)
# Image can be read only when RTS is Low (False)
# Exposure can not be less than 0.03

# Useful information:http://www.lavrsen.dk/foswiki/bin/view/PWC/ApplicationProgrammingInterface
# It looks like 5 fps can only be achieved at low resolutions less than 320x240

import cv2, time
import serial
import serial.tools.list_ports
import re
# Stremer imports
import base64
import zmq
from struct import *
import json
import threading

global running
running = False

# Recently added
#------------------------------------------------------------------------
def OpenSerialPort(baudRate):
    ini = False
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        # if 'USB and Serial' in p.description:
        search_result = re.search(r'USB.*Serial', p.description, re.M | re.I)
        if search_result != None:
            print ("Opening serial port: ",p.device)
            Port = p.device
            ini = True  # Finds USB to Serial port
    if not ini:
        return (ini,'')  # Did not find USB to Serial port
    try:
        ser = serial.Serial(port=Port, baudrate=baudRate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE, timeout=5, rtscts=0)
    except IOError as e:
        ini = False  # Error opening the serial port
        print (e)
    if ini:
        ser.isOpen()  # If there was no error open the serial chanel
    return (ini,ser)
#------------------------------------------------------------------------
def image_proc(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

# def lx(exp=0.05,gain=0,thr=70):
def lx():
    global running

    global exp
    global gain
    global thr

    exp = exposure
    thr = threshold

    #------------------- Prepare streaming-------------------------
    context = zmq.Context()
    footage_socket = context.socket(zmq.PUB)
    footage_socket.bind('tcp://*:5555')
    #--------------------------------------------------------------
    
    THRESHOLD = thr

    status,ser = OpenSerialPort(115200)
    #print ("Opening serial port: ","/dev/ttyUSB0")
    if not status:
        exit()
    '''
    # This section was only working for raspberry pi. I changed to work also with PC adding the function  
    # OpenSerialPort(115200)
    
    serialPort = "/dev/ttyUSB0"
    #Open the serial port
    ser = serial.Serial()
    ser.port = serialPort
    ser.baudrate = 115200

    ser.open()
    '''


    #Stop Exposure

    #ser.setDTR(False)
    ser.setRTS(True)

    print("starting video capture")
    cap=cv2.VideoCapture(0)
    time.sleep(0.5)

    if not cap.isOpened():  # check if we succeeded
        print("error opening video capture")
        exit() 

    cap.set(cv2.CAP_PROP_GAIN, gain)
    #cap.set(cv2.CAP_PROP_SATURATION,0.0)
    #cap.set(cv2.CAP_PROP_CONTRAST,32.0)



    #cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.0)

    #CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
    #CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
    #print("CAP_PROP_POS_FRAMES = ",cap.get(cv2.CAP_PROP_POS_FRAMES))
    print("CAP_PROP_POS_MSEC = ",cap.get(cv2.CAP_PROP_POS_MSEC))
    
    print("CAP_PROP_FRAME_WIDTH = " , cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("CAP_PROP_FRAME_HEIGHT", cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    print("CAP_PROP_FRAME_WIDTH = " , cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("CAP_PROP_FRAME_HEIGHT", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    #cap.set(cv2.CAP_PROP_FPS,5)         
    print ("CAP_PROP_FPS = ", cap.get(cv2.CAP_PROP_FPS))#CAP_PROP_FPS Frame rate.

    print ("CAP_PROP_FOURCC",cap.get(cv2.CAP_PROP_FOURCC))#CAP_PROP_FOURCC 4-character code of codec.
    
    
    
    #print ("CAP_PROP_FRAME_COUNT = ", cap.get(cv2.CAP_PROP_FRAME_COUNT)) #CAP_PROP_FRAME_COUNT Number of frames in the video file.
    #CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
    print ("CAP_PROP_MODE ",cap.get(cv2.CAP_PROP_MODE)) #CAP_PROP_MODE Backend-specific value indicating the current capture mode.
    print("CAP_PROP_BRIGHTNESS", cap.get(cv2.CAP_PROP_BRIGHTNESS))  #CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
    print("CAP_PROP_CONTRAST",cap.get(cv2.CAP_PROP_CONTRAST))       #CAP_PROP_CONTRAST Contrast of the image (only for cameras).
    brt=50
    good_brt=brt
    cap.set(cv2.CAP_PROP_BRIGHTNESS,brt)
    print("CAP_PROP_SATURATION",cap.get(cv2.CAP_PROP_SATURATION))#CAP_PROP_SATURATION Saturation of the image (only for cameras).
    #print("CAP_PROP_HUE",cap.get(cv2.CAP_PROP_HUE))#CAP_PROP_HUE Hue of the image (only for cameras).
    print("CAP_PROP_GAIN",cap.get(cv2.CAP_PROP_GAIN))      #CAP_PROP_GAIN Gain of the image (only for cameras).
    #print("CAP_PROP_EXPOSURE = ", cap.get(cv2.CAP_PROP_EXPOSURE))#CAP_PROP_EXPOSURE Exposure (only for cameras).
    #print("CAP_PROP_AUTO_EXPOSURE",cap.get(cv2.CAP_PROP_AUTO_EXPOSURE))

    print("CAP_PROP_CONVERT_RGB",cap.get(cv2.CAP_PROP_CONVERT_RGB))#CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
    #print("CAP_PROP_WHITE_BALANCE ",cap.get(cv2.CAP_PROP_WHITE_BALANCE)) #CAP_PROP_WHITE_BALANCE Currently not supported
    #CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

    n = 0
    pct=100
    ser.setRTS(True)
    time.sleep(exp)
    ser.setRTS(False)
    time.sleep(5.0/1000)
    check,frame = cap.read()
    time.sleep(10.0/1000)
    cv2.waitKey(1)
    
    good_frame = 0.0
    bad_frame = 0

    while (running):
        #Before activate long exposure I have to set Auto exposure off
        # and  other parameters also off
        old = 0
          
        ser.setRTS(True)  # Start Exposure
        begin = time.time()    # Time in seconds
        if cv2.waitKey(int(exp*1000)) & 0xFF == ord('q'):
            break
        ser.setRTS(False)  # Stop Exposure
        
        end1 = time.time()
        for i in range(6):
            check,frame = cap.read()
            time.sleep(0.1)
            #cv2.waitKey(50) 
            if check:
                g_image = image_proc(frame)
                
                s = cv2.mean(g_image)                    
                new = s[0]
                #print("old & new",int(old),int(new))
                
                if new > old:
                    brightImage = frame
                    g_brightImage=g_image
                    old = new
                    if old>THRESHOLD:
                        good_frame = good_frame+1.0
                        break
                    
        print("Captured Image",n+1,"Light Level ",int(old))
        
        end = time.time()
        print("Duration",end-begin, "Shutter Speed=",end1-begin)
        if old>THRESHOLD+5:
            # Display brightest image
            print("Display Image",n+1,"Light Level ",int(old),"Brightness",brt)
#            cv2.imshow("Local",brightImage)
            if old>THRESHOLD:
                #brt=brt*0.95
                good_brt=brt
                brt-=1
                cap.set(cv2.CAP_PROP_BRIGHTNESS,brt)
            else:
                #brt=brt*1.05
                if old<THRESHOLD:
                    brt+=1
                    cap.set(cv2.CAP_PROP_BRIGHTNESS,brt)
#-------------------------  Streaming ------------------------
            encoded, buffer = cv2.imencode('.jpg',brightImage )
            jpg_as_text = base64.b64encode(buffer)

            topic = "frame"
            footage_socket.send_string(topic,zmq.SNDMORE)
            footage_socket.send(jpg_as_text)
# -------------------------  Streaming ------------------------
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            brt+=1
            cap.set(cv2.CAP_PROP_BRIGHTNESS,brt)
            bad_frame+=1
        if n>0:
            pct=good_frame/(n+1)*100
            print("% Good Frames", int(pct),"N_Good Frames = ",good_frame)
        n=n+1
        #---------------------- Streaming ------------------------------
        topic = "status"
        footage_socket.send_string(topic, zmq.SNDMORE)
        status = {"goodFrames": good_frame,
                  "avgLight": int(old), "brightness": brt, "pctGoodFrames": pct}
        footage_socket.send_json(status)
        #---------------------- Streaming -------------------------------
        if bad_frame>5:
            #print("Good_brt",good_brt,brt)
            cap.set(cv2.CAP_PROP_BRIGHTNESS,good_brt+1)
            good_brt+=1
            bad_frame -= 1


    #Stop Exposure

    ser.setRTS(False)

    ser.close()
    cap.release()
    # Line below Only required if a cv2.imshow created a window
    # cv2.destroyAllWindows()



# if __name__ == "__main__":
#     global running
#     exposure = float(sys.argv[1])
#     gain = float(sys.argv[2])
#     if len(sys.argv) <= 3:
#         thr=70
#     else:
#         thr=int(sys.argv[3])
#     fps = exposure/2
#     running = True
#     # create a thread and run lx in the thread
#     # open a socket to receive lx parameters from remote client
#     # put the socket in a loop and receive parameters or a finish commad
#     lx(exposure, gain,thr)


if __name__ == "__main__":
    running = True
    # create a thread and run lx in the thread
    # open a socket to receive lx parameters from remote client
    # put the socket in a loop and receive parameters or a finish commad

    global exp
    global gain
    global thr

    context = zmq.Context()
    command_socket = context.socket(zmq.SUB)
    command_socket.bind('tcp://*:5556')
    #command_socket.setsockopt(zmq.SUBSCRIBE,b'camara_settings')
    #command_socket.setsockopt(zmq.SUBSCRIBE, b'start')
    #command_socket.setsockopt(zmq.SUBSCRIBE, b'stop')
    command_socket.setsockopt(zmq.SUBSCRIBE, b'')
    while True:
        # check for commands from UI
        topic_cmd = command_socket.recv_multipart()
        topic = topic_cmd[0].decode('ascii')
        print("Command received",topic)
        if topic == 'camara_settings':
            str_commands = topic_cmd[1].decode('ascii')
            print("Str_Commnads = ",str_commands)
            ui_commands = json.loads(str_commands)
            exposure = ui_commands['exposure']
            gain_ = ui_commands['gain']
            threshold = ui_commands['threshold']
            print("Settings = ",exposure,gain,threshold)
        elif topic == 'stop':
            print("Stopped")
            running = False
            print("ready wait for tread to join")
            command_thread.join()
            print("tread joined")
        elif topic == 'start':
            running = True
            print("Started")
            str_commands = topic_cmd[1].decode('ascii')
            print("Str_Commnads rx ",str_commands)
            ui_commands = json.loads(str_commands)
            exposure = float(ui_commands['exposure'])
            gain = int(ui_commands['gain'])
            threshold = int(ui_commands['threshold'])

<<<<<<< HEAD
            print("Settings to lx = ",exposure,gain,threshold)
            command_thread = threading.Thread(target=lx, args=(exposure, gain, threshold))
=======
            print("Settings = ",exposure,gain,threshold)
            # command_thread = threading.Thread(target=lx, args=(exposure, gain, threshold))
            command_thread = threading.Thread(target=lx)
>>>>>>> 535e60bcedd91ffef1a7619d1f34b128c554b6c1
            command_thread.start()

