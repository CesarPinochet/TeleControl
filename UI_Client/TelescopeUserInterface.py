import base64
import datetime
import json
import threading
from time import strftime, localtime

import cv2
import numpy as np
import zmq

from initialSetUp import configVariables as cfgv


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *

from TelescopeTcpClientClass import *
from ui_TelControlWindow import Ui_MainWindow

running = False
capture_thread = None

class TelControlWindow(QMainWindow, Ui_MainWindow):
    '''User Interface to control an MEADE ETX90-C and capture images via a webcam'''
    # see in this link how to implement double inheritancce for QMainWindow
    # https: // www.riverbankcomputing.com / static / Docs / PyQt5 / designer.html
    # and how to insert the Qt designed UI
    def __init__(self):
        super(TelControlWindow, self).__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)
        # --------------------------------------------------------------
        init = cfgv.initialSetUp()
        # raspberryPiAddr = '192.168.11.252'
        self.raspberryPiAddr = init.raspberryPiAddr
        context = zmq.Context()
        self.commands_socket = context.socket(zmq.PUB)
        self.commands_socket.connect("tcp://%s:5556" % self.raspberryPiAddr)
        # --------------------------------------------------------------

# The closseEvent triggers when user try to the window
# This overides method in Main Window
    def closeEvent(self, event):
        global running
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            running = False
            event.accept()
        else:
            event.ignore()


    def telChnlSend(self, msg):
        # If all modules are running in the same machine do not pass an ip address to RemoteTcpConnect()
        # Or pass 'localhost'

        telChnl = RemoteTcpConnect('192.168.11.252')
        if telChnl.connect() == False:
            print "Error Opening channel to remote telescope"
            quit()
        return (telChnl.send_msg(msg))

    def move_up(self):
        self.telChnlSend("Up%")

    def stop_up(self):
        self.telChnlSend("Stop_Up%")

    def move_down(self):
        self.telChnlSend("Down%")

    def stop_down(self):
        self.telChnlSend("Stop_Down%")

    def move_left(self):
        self.telChnlSend("Left%")

    def stop_left(self):
        self.telChnlSend("Stop_Left%")

    def move_right(self):
        self.telChnlSend("Right%")

    def stop_right(self):
        self.telChnlSend("Stop_Right%")

    def speed1(self):
        self.telChnlSend("Speed1%")

    def speed2(self):
        self.telChnlSend("Speed2%")

    def speed3(self):
        self.telChnlSend("Speed3%")

    def speed4(self):
        self.telChnlSend("Speed4%")

    def getTimeDate(self):
        tday = datetime.date.today()
        now = datetime.datetime.now()
        self.timeEdit_SetLocalTime.setTime(QtCore.QTime(now.hour, now.minute, now.second))
        self.dateEdit_SetLocalDate.setDate(QtCore.QDate(tday.year, tday.month, tday.day))

    def SetTelescopeData(self):
        # '%' Separates command form argument
        # If % is the end of command,menas there is no argument
        cmd = "TelescopeDate" + "%" + strftime("%m/%d/%y", localtime())
        self.telChnlSend(cmd)

        cmd = "LocalTime" + "%" + strftime("%H:%M:%S", localtime())
        self.telChnlSend(cmd)

    def halt(self):
        self.telChnlSend("StopGoTo%")

    def park(self):
        self.telChnlSend("Park%")

    def TelSleep(self):
        self.telChnlSend("TelSleep%")

    def alignTelescope(self):
        cmd = self.telChnlSend("AlignTelescope%")
        if cmd == 0:
            print("AlignTelescope ERROR")
            quit()

    def go_home(self):
        return

    def set_mode(self):
        return

    def updateVideoCapStatus(self,ip_R_PI):
        '''Open a subscriber socket to connect to the R_Pi and wait for topic = status to receive data about:
         VALID FRAMES, BRIGHTNESS &  PERCENTAGE OF GOOD FREMES CAPTURED.
         Data is received at the same rate as exposure, example:
         if exposure is 0.1sec the status will be updated each 0.1sec

         '''
        global running
        print("Inicio Update video Status")
        context = zmq.Context()
        video_Status_socket = context.socket(zmq.SUB)
        video_Status_socket.connect("tcp://%s:5555" % ip_R_PI)
        topic = "status"
        video_Status_socket.setsockopt(zmq.SUBSCRIBE, topic)
        while running:
            topic_status = video_Status_socket.recv_multipart()
            str_dict = topic_status[1]
            status = json.loads(str_dict)

            #print (status)
            #print ("Number of Good Frames = %.1f AVG Light Level = %d Brightness = %d  pct Good Frames = %d" \
            #       % (status['goodFrames'], status['avgLight'], \
            #         status['brightness'], status['pctGoodFrames']))
            window.lineEdit_Avg_Brightness.setText(str(status['avgLight']))
            window.lineEdit_Frame_Captured.setText(str(status['goodFrames']))
            window.lineEdit_pct_GoodFrames.setText(str(status['pctGoodFrames']))
        print("Recibio Close - Video Update status")
        #video_Status_socket.close()
        #context.destroy(0)

    def ActivateVideo(self):
        '''Open a thread to connect to raspberryPi and send a command to adtivate video streamming.'''
        global running

        # init = cfgv.initialSetUp()
        # # raspberryPiAddr = '192.168.11.252'
        # raspberryPiAddr = init.raspberryPiAddr

        if self.pushButton_Activate_Video.isChecked():
            running = True

            streming_thread = threading.Thread(target=streamVideo, args=(self.raspberryPiAddr,))
            updateVideoCaptureStatus_thread = threading.Thread(target=self.updateVideoCapStatus, args=(self.raspberryPiAddr,))
            streming_thread.start()
            updateVideoCaptureStatus_thread.start()
            # --------------------------------------------------------------
            # context = zmq.Context()
            # self.commands_socket = context.socket(zmq.PUB)
            # self.commands_socket.connect("tcp://%s:5556" % raspberryPiAddr)
            topic = "start"
            self.commands_socket.send_string(topic, zmq.SNDMORE)
            status = {"exposure": self.doubleSpinBox_Exposure.value(),"gain":self.spinBox_Gain.value(),"threshold":self.spinBox_Threshold.value()}
            self.commands_socket.send_json(status)
            # --------------------------------------------------------------
            self.pushButton_Activate_Video.setText('Started...')

        else:
            running = False
            topic = "stop"
            self.commands_socket.send_string(topic)
            self.pushButton_Activate_Video.setText('Stopped...')
        return

    def copyToFile(self):
        return
    def set_exposure(self):
        # --------------------------------------------------------------
        topic = "camara_settings"
        self.commands_socket.send_string(topic, zmq.SNDMORE)
        status = {"exposure": self.doubleSpinBox_Exposure.value(), "gain": self.spinBox_Gain.value(),
                  "threshold": self.spinBox_Threshold.value()}
        self.commands_socket.send_json(status)

        # --------------------------------------------------------------

    def set_gain(self):
        self.set_exposure()
    def set_threshold(self):
        self.set_exposure()

    # def SnapShot(self):
    #    #cap = cv2.VideoCapture(0)
    #    #check, frame = cap.read()
    #    return
    def GetTelescopeInfo(self):
        telDateTime = self.telChnlSend("GetTelTimeDate%")
        print ("Date & time ", telDateTime)
        # Receive this format: 17:00:24#%06/16/18#|
        msgTime = telDateTime[:8]  # Takes the first 8 characters 17:00:24
        msgDt = telDateTime[10:18]  # Takes the date 06/16/18
        msgDate = msgDt[3:6] + msgDt[:3] + "20" + msgDt[6:8]  # Transform date from 06/16/18 to 16/06/2018

        #self.lineEdit_TelTime.setText(QtCore.QTime.fromString(msgTime, "hh:mm:ss"))
        self.lineEdit_TelTime.setText(msgTime)
        #self.lineEdit_TelDate.setText(QtCore.QDate.fromString(msgDate, "dd/MM/yyyy"))
        self.lineEdit_TelDate.setText(msgDate)

        telRA = self.telChnlSend("GetTelRA%")
        self.lineEdit_TelRA.setText(telRA[:8])

        msgRcv = self.telChnlSend("GetTelDEC%")
        telDEC = msgRcv[:3] + "d " + msgRcv[4:6] + "m " + msgRcv[7:9] + "s"
        self.lineEdit_TelDEC.setText(telDEC)

        siteName = self.telChnlSend("GetTelSiteName%")
        self.lineEdit_TelSiteName.setText(siteName[:-1])

        msgRcv = self.telChnlSend("GetTelAlignment%")
        algn = {
            'A': 'Az',
            'P': 'Eqt',
            'G': 'Ger',
            'T': 'Tracking',
            'N': 'No Tracking',
            '0': 'NeedsAlign',
            '1': '1-Star Alng',
            '2': '2-Star Alng',
            '3': '3-Star Alng'
        }
        ALGN = algn[msgRcv[0:1]] + "," + algn[msgRcv[1:2]] + "," + algn[msgRcv[2:3]]
        self.lineEdit_TelAlignment.setText(ALGN)

        AZM = self.telChnlSend("GetTelAzimuth%")
        self.lineEdit_TelAzimuth.setText(AZM[:3] + " " + AZM[4:-1])

        ALT = self.telChnlSend("GetTelAltitud%")
        self.lineEdit_TelAltitud.setText(ALT[:3] + " " + ALT[4:-1])

        # Site Longitud and Latitude
        msgRcv = self.telChnlSend("GetSiteLatitude%")
        S_LAT = msgRcv[:3] + "d " + msgRcv[4:9] + "m "
        self.lineEdit_SiteLatitude.setText(S_LAT)

        msgRcv = self.telChnlSend("GetSiteLongitude%")
        S_LONG = msgRcv[:3] + "d " + msgRcv[4:9] + "m "
        self.lineEdit_SiteLongitud.setText(S_LONG)



def streamVideo(ip_R_PI):
    '''Connect to the remote camera using a Subscriber socket and display video.'''
    global running
    context = zmq.Context()
    footage_socket = context.socket(zmq.SUB)
    footage_socket.connect("tcp://%s:5555" % ip_R_PI)
    topic = "frame"
    footage_socket.setsockopt(zmq.SUBSCRIBE, topic)
    print ("Inicio stream video")
    while running:
        topic_frame = footage_socket.recv_multipart()
        #print ("Topic_rcv = %s" % topic_frame[0])
        frame = topic_frame[1]
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        # black_white = cv2.imdecode(npimg,0) # Estaba en 1
        # cv2.imshow("NoEq", black_white)
        color = cv2.imdecode(npimg,1)
        cv2.imshow("COLOR", color)
        cv2.waitKey(1)
    print("Recibio Close streamVideo")
    #footage_socket.close()
    #context.destroy(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication([])
    # Define the windows style/appearance
    # The string must typically one of "windows", "motif", "cde", "plastique", "windowsxp", or "macintosh".
    # Style names are case insensitive.
    app.setStyle("windows")
    window = TelControlWindow()
    window.show()
    app.exit(app.exec_())