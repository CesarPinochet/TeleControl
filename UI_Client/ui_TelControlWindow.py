# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PythonProjects_Git\TeleControl\UI_Client\TelescopeUserInterface.ui'
#
# Created by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(680, 550)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/mono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_TelMovement = QtGui.QVBoxLayout()
        self.verticalLayout_TelMovement.setObjectName(_fromUtf8("verticalLayout_TelMovement"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_Speed2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Speed2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Speed2.setObjectName(_fromUtf8("pushButton_Speed2"))
        self.gridLayout.addWidget(self.pushButton_Speed2, 0, 2, 1, 1)
        self.pushButton_LeftArrow = QtGui.QPushButton(self.centralwidget)
        self.pushButton_LeftArrow.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_LeftArrow.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LeftArrow.setIcon(icon1)
        self.pushButton_LeftArrow.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_LeftArrow.setObjectName(_fromUtf8("pushButton_LeftArrow"))
        self.gridLayout.addWidget(self.pushButton_LeftArrow, 1, 0, 1, 1)
        self.pushButton_RightArrow = QtGui.QPushButton(self.centralwidget)
        self.pushButton_RightArrow.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_RightArrow.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_RightArrow.setIcon(icon2)
        self.pushButton_RightArrow.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_RightArrow.setObjectName(_fromUtf8("pushButton_RightArrow"))
        self.gridLayout.addWidget(self.pushButton_RightArrow, 1, 2, 1, 1)
        self.pushButton_Home = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Home.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Home.setObjectName(_fromUtf8("pushButton_Home"))
        self.gridLayout.addWidget(self.pushButton_Home, 1, 1, 1, 1)
        self.pushButton_DownArrow = QtGui.QPushButton(self.centralwidget)
        self.pushButton_DownArrow.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_DownArrow.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_DownArrow.setIcon(icon3)
        self.pushButton_DownArrow.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_DownArrow.setObjectName(_fromUtf8("pushButton_DownArrow"))
        self.gridLayout.addWidget(self.pushButton_DownArrow, 2, 1, 1, 1)
        self.pushButton_Speed4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Speed4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Speed4.setObjectName(_fromUtf8("pushButton_Speed4"))
        self.gridLayout.addWidget(self.pushButton_Speed4, 2, 2, 1, 1)
        self.pushButton_Speed1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Speed1.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Speed1.setObjectName(_fromUtf8("pushButton_Speed1"))
        self.gridLayout.addWidget(self.pushButton_Speed1, 0, 0, 1, 1)
        self.pushButton_UpArrow = QtGui.QPushButton(self.centralwidget)
        self.pushButton_UpArrow.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_UpArrow.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_UpArrow.setIcon(icon4)
        self.pushButton_UpArrow.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_UpArrow.setObjectName(_fromUtf8("pushButton_UpArrow"))
        self.gridLayout.addWidget(self.pushButton_UpArrow, 0, 1, 1, 1)
        self.pushButton_Speed3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Speed3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Speed3.setObjectName(_fromUtf8("pushButton_Speed3"))
        self.gridLayout.addWidget(self.pushButton_Speed3, 2, 0, 1, 1)
        self.verticalLayout_TelMovement.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Park = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Park.setObjectName(_fromUtf8("pushButton_Park"))
        self.horizontalLayout.addWidget(self.pushButton_Park)
        self.pushButton_Sleep = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Sleep.setObjectName(_fromUtf8("pushButton_Sleep"))
        self.horizontalLayout.addWidget(self.pushButton_Sleep)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_StopGoTo = QtGui.QPushButton(self.centralwidget)
        self.pushButton_StopGoTo.setObjectName(_fromUtf8("pushButton_StopGoTo"))
        self.verticalLayout_2.addWidget(self.pushButton_StopGoTo)
        self.pushButton_AlignTelescope = QtGui.QPushButton(self.centralwidget)
        self.pushButton_AlignTelescope.setObjectName(_fromUtf8("pushButton_AlignTelescope"))
        self.verticalLayout_2.addWidget(self.pushButton_AlignTelescope)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_TelMovement.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_TelMovement, 0, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setLineWidth(3)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 0, 4, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setLineWidth(3)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.spinBox_setSiteLongitudeDegrees = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_setSiteLongitudeDegrees.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.spinBox_setSiteLongitudeDegrees.setMaximum(359)
        self.spinBox_setSiteLongitudeDegrees.setObjectName(_fromUtf8("spinBox_setSiteLongitudeDegrees"))
        self.gridLayout_3.addWidget(self.spinBox_setSiteLongitudeDegrees, 5, 0, 1, 1)
        self.label_SystemTime = QtGui.QLabel(self.centralwidget)
        self.label_SystemTime.setObjectName(_fromUtf8("label_SystemTime"))
        self.gridLayout_3.addWidget(self.label_SystemTime, 0, 0, 1, 1)
        self.timeEdit_SetLocalTime = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit_SetLocalTime.setEnabled(True)
        self.timeEdit_SetLocalTime.setAutoFillBackground(False)
        self.timeEdit_SetLocalTime.setSpecialValueText(_fromUtf8(""))
        self.timeEdit_SetLocalTime.setDate(QtCore.QDate(2000, 1, 1))
        self.timeEdit_SetLocalTime.setTime(QtCore.QTime(18, 59, 59))
        self.timeEdit_SetLocalTime.setObjectName(_fromUtf8("timeEdit_SetLocalTime"))
        self.gridLayout_3.addWidget(self.timeEdit_SetLocalTime, 0, 1, 1, 1)
        self.dateEdit_SetLocalDate = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_SetLocalDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 7), QtCore.QTime(3, 0, 0)))
        self.dateEdit_SetLocalDate.setTime(QtCore.QTime(3, 0, 0))
        self.dateEdit_SetLocalDate.setObjectName(_fromUtf8("dateEdit_SetLocalDate"))
        self.gridLayout_3.addWidget(self.dateEdit_SetLocalDate, 1, 1, 1, 1)
        self.label_SetTelSiteLatitude = QtGui.QLabel(self.centralwidget)
        self.label_SetTelSiteLatitude.setObjectName(_fromUtf8("label_SetTelSiteLatitude"))
        self.gridLayout_3.addWidget(self.label_SetTelSiteLatitude, 7, 0, 1, 1)
        self.spinBox_setSiteLatitudeMinutes = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_setSiteLatitudeMinutes.setMaximum(59)
        self.spinBox_setSiteLatitudeMinutes.setObjectName(_fromUtf8("spinBox_setSiteLatitudeMinutes"))
        self.gridLayout_3.addWidget(self.spinBox_setSiteLatitudeMinutes, 8, 1, 1, 1)
        self.lineEdit_SetLocation = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SetLocation.setObjectName(_fromUtf8("lineEdit_SetLocation"))
        self.gridLayout_3.addWidget(self.lineEdit_SetLocation, 2, 1, 1, 1)
        self.label_SystemDate = QtGui.QLabel(self.centralwidget)
        self.label_SystemDate.setObjectName(_fromUtf8("label_SystemDate"))
        self.gridLayout_3.addWidget(self.label_SystemDate, 1, 0, 1, 1)
        self.spinBox_setSiteLatitudeDegrees = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_setSiteLatitudeDegrees.setMinimum(-180)
        self.spinBox_setSiteLatitudeDegrees.setMaximum(180)
        self.spinBox_setSiteLatitudeDegrees.setObjectName(_fromUtf8("spinBox_setSiteLatitudeDegrees"))
        self.gridLayout_3.addWidget(self.spinBox_setSiteLatitudeDegrees, 8, 0, 1, 1)
        self.spinBox_setSiteLongitudMinutes = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_setSiteLongitudMinutes.setMaximum(59)
        self.spinBox_setSiteLongitudMinutes.setObjectName(_fromUtf8("spinBox_setSiteLongitudMinutes"))
        self.gridLayout_3.addWidget(self.spinBox_setSiteLongitudMinutes, 5, 1, 1, 1)
        self.label_SetLocation = QtGui.QLabel(self.centralwidget)
        self.label_SetLocation.setObjectName(_fromUtf8("label_SetLocation"))
        self.gridLayout_3.addWidget(self.label_SetLocation, 2, 0, 1, 1)
        self.comboBox_TrackingMode = QtGui.QComboBox(self.centralwidget)
        self.comboBox_TrackingMode.setObjectName(_fromUtf8("comboBox_TrackingMode"))
        self.comboBox_TrackingMode.addItem(_fromUtf8(""))
        self.comboBox_TrackingMode.addItem(_fromUtf8(""))
        self.comboBox_TrackingMode.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_TrackingMode, 3, 1, 1, 1)
        self.label_TelTrackingMode = QtGui.QLabel(self.centralwidget)
        self.label_TelTrackingMode.setObjectName(_fromUtf8("label_TelTrackingMode"))
        self.gridLayout_3.addWidget(self.label_TelTrackingMode, 3, 0, 1, 1)
        self.label_SetTelSiteLongitude = QtGui.QLabel(self.centralwidget)
        self.label_SetTelSiteLongitude.setObjectName(_fromUtf8("label_SetTelSiteLongitude"))
        self.gridLayout_3.addWidget(self.label_SetTelSiteLongitude, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_GetTimeDate = QtGui.QPushButton(self.centralwidget)
        self.pushButton_GetTimeDate.setObjectName(_fromUtf8("pushButton_GetTimeDate"))
        self.horizontalLayout_2.addWidget(self.pushButton_GetTimeDate)
        self.pushButton_SetTelescopeData = QtGui.QPushButton(self.centralwidget)
        self.pushButton_SetTelescopeData.setObjectName(_fromUtf8("pushButton_SetTelescopeData"))
        self.horizontalLayout_2.addWidget(self.pushButton_SetTelescopeData)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setLineWidth(3)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 1, 2, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setLineWidth(3)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 1, 3, 1, 3)
        self.gridLayout_CamaraViewer = QtGui.QGridLayout()
        self.gridLayout_CamaraViewer.setObjectName(_fromUtf8("gridLayout_CamaraViewer"))
        self.lineEdit_FileName = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_FileName.setObjectName(_fromUtf8("lineEdit_FileName"))
        self.gridLayout_CamaraViewer.addWidget(self.lineEdit_FileName, 2, 0, 1, 2)
        self.label_VideoCapture = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_VideoCapture.setFont(font)
        self.label_VideoCapture.setObjectName(_fromUtf8("label_VideoCapture"))
        self.gridLayout_CamaraViewer.addWidget(self.label_VideoCapture, 0, 0, 1, 1)
        self.spinBox_Gain = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_Gain.setMaximum(255)
        self.spinBox_Gain.setObjectName(_fromUtf8("spinBox_Gain"))
        self.gridLayout_CamaraViewer.addWidget(self.spinBox_Gain, 4, 1, 1, 1)
        self.doubleSpinBox_Exposure = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_Exposure.setMinimum(0.04)
        self.doubleSpinBox_Exposure.setMaximum(300.0)
        self.doubleSpinBox_Exposure.setSingleStep(0.5)
        self.doubleSpinBox_Exposure.setObjectName(_fromUtf8("doubleSpinBox_Exposure"))
        self.gridLayout_CamaraViewer.addWidget(self.doubleSpinBox_Exposure, 3, 1, 1, 1)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_CamaraViewer.addWidget(self.line_6, 6, 0, 1, 2)
        self.spinBox_Threshold = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_Threshold.setMaximum(255)
        self.spinBox_Threshold.setProperty("value", 50)
        self.spinBox_Threshold.setObjectName(_fromUtf8("spinBox_Threshold"))
        self.gridLayout_CamaraViewer.addWidget(self.spinBox_Threshold, 5, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_CamaraViewer.addItem(spacerItem4, 11, 0, 1, 1)
        self.label_Gain = QtGui.QLabel(self.centralwidget)
        self.label_Gain.setObjectName(_fromUtf8("label_Gain"))
        self.gridLayout_CamaraViewer.addWidget(self.label_Gain, 4, 0, 1, 1)
        self.label_Threshold = QtGui.QLabel(self.centralwidget)
        self.label_Threshold.setObjectName(_fromUtf8("label_Threshold"))
        self.gridLayout_CamaraViewer.addWidget(self.label_Threshold, 5, 0, 1, 1)
        self.label_Exposure = QtGui.QLabel(self.centralwidget)
        self.label_Exposure.setObjectName(_fromUtf8("label_Exposure"))
        self.gridLayout_CamaraViewer.addWidget(self.label_Exposure, 3, 0, 1, 1)
        self.lineEdit_Avg_Brightness = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Avg_Brightness.setObjectName(_fromUtf8("lineEdit_Avg_Brightness"))
        self.gridLayout_CamaraViewer.addWidget(self.lineEdit_Avg_Brightness, 8, 1, 1, 1)
        self.label_AvgBrightness = QtGui.QLabel(self.centralwidget)
        self.label_AvgBrightness.setObjectName(_fromUtf8("label_AvgBrightness"))
        self.gridLayout_CamaraViewer.addWidget(self.label_AvgBrightness, 8, 0, 1, 1)
        self.lineEdit_Frame_Captured = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Frame_Captured.setObjectName(_fromUtf8("lineEdit_Frame_Captured"))
        self.gridLayout_CamaraViewer.addWidget(self.lineEdit_Frame_Captured, 9, 1, 1, 1)
        self.lineEdit_pct_GoodFrames = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pct_GoodFrames.setObjectName(_fromUtf8("lineEdit_pct_GoodFrames"))
        self.gridLayout_CamaraViewer.addWidget(self.lineEdit_pct_GoodFrames, 10, 1, 1, 1)
        self.label_FrameCaptured = QtGui.QLabel(self.centralwidget)
        self.label_FrameCaptured.setObjectName(_fromUtf8("label_FrameCaptured"))
        self.gridLayout_CamaraViewer.addWidget(self.label_FrameCaptured, 9, 0, 1, 1)
        self.label_pctGoodFrames = QtGui.QLabel(self.centralwidget)
        self.label_pctGoodFrames.setObjectName(_fromUtf8("label_pctGoodFrames"))
        self.gridLayout_CamaraViewer.addWidget(self.label_pctGoodFrames, 10, 0, 1, 1)
        self.pushButton_Activate_Video = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Activate_Video.setCheckable(True)
        self.pushButton_Activate_Video.setObjectName(_fromUtf8("pushButton_Activate_Video"))
        self.gridLayout_CamaraViewer.addWidget(self.pushButton_Activate_Video, 1, 0, 1, 1)
        self.radioButton_CopyToFile = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_CopyToFile.setChecked(False)
        self.radioButton_CopyToFile.setObjectName(_fromUtf8("radioButton_CopyToFile"))
        self.gridLayout_CamaraViewer.addWidget(self.radioButton_CopyToFile, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_CamaraViewer, 0, 5, 1, 1)
        self.gridLayout_TescopeInfo = QtGui.QGridLayout()
        self.gridLayout_TescopeInfo.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_TescopeInfo.setObjectName(_fromUtf8("gridLayout_TescopeInfo"))
        self.label_TelSiteLatitude = QtGui.QLabel(self.centralwidget)
        self.label_TelSiteLatitude.setObjectName(_fromUtf8("label_TelSiteLatitude"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelSiteLatitude, 5, 1, 1, 1)
        self.label_TelescopeInfo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_TelescopeInfo.setFont(font)
        self.label_TelescopeInfo.setObjectName(_fromUtf8("label_TelescopeInfo"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelescopeInfo, 2, 0, 1, 1)
        self.lineEdit_TelRA = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelRA.setObjectName(_fromUtf8("lineEdit_TelRA"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelRA, 10, 0, 1, 1)
        self.lineEdit_TelSlewRate = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelSlewRate.setObjectName(_fromUtf8("lineEdit_TelSlewRate"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelSlewRate, 10, 2, 1, 1)
        self.label_TelDec = QtGui.QLabel(self.centralwidget)
        self.label_TelDec.setObjectName(_fromUtf8("label_TelDec"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelDec, 8, 1, 1, 1)
        self.label_TelSlewRate = QtGui.QLabel(self.centralwidget)
        self.label_TelSlewRate.setObjectName(_fromUtf8("label_TelSlewRate"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelSlewRate, 8, 2, 1, 1)
        self.label_TelAltitud = QtGui.QLabel(self.centralwidget)
        self.label_TelAltitud.setObjectName(_fromUtf8("label_TelAltitud"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelAltitud, 11, 0, 1, 1)
        self.lineEdit_TelAltitud = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelAltitud.setObjectName(_fromUtf8("lineEdit_TelAltitud"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelAltitud, 12, 0, 1, 1)
        self.label_TelTime = QtGui.QLabel(self.centralwidget)
        self.label_TelTime.setObjectName(_fromUtf8("label_TelTime"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelTime, 3, 1, 1, 1)
        self.lineEdit_TelAlignment = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelAlignment.setObjectName(_fromUtf8("lineEdit_TelAlignment"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelAlignment, 4, 2, 1, 1)
        self.label_TelAligment = QtGui.QLabel(self.centralwidget)
        self.label_TelAligment.setObjectName(_fromUtf8("label_TelAligment"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelAligment, 3, 2, 1, 1)
        self.pushButton_GetTel_Info = QtGui.QPushButton(self.centralwidget)
        self.pushButton_GetTel_Info.setObjectName(_fromUtf8("pushButton_GetTel_Info"))
        self.gridLayout_TescopeInfo.addWidget(self.pushButton_GetTel_Info, 13, 0, 1, 1)
        self.label_TelRA = QtGui.QLabel(self.centralwidget)
        self.label_TelRA.setObjectName(_fromUtf8("label_TelRA"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelRA, 8, 0, 1, 1)
        self.lineEdit_SiteLongitud = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SiteLongitud.setObjectName(_fromUtf8("lineEdit_SiteLongitud"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_SiteLongitud, 6, 2, 1, 1)
        self.lineEdit_TelDEC = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelDEC.setObjectName(_fromUtf8("lineEdit_TelDEC"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelDEC, 10, 1, 1, 1)
        self.label_TelAzimuth = QtGui.QLabel(self.centralwidget)
        self.label_TelAzimuth.setObjectName(_fromUtf8("label_TelAzimuth"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelAzimuth, 11, 1, 1, 1)
        self.label_TelSiteLongitude = QtGui.QLabel(self.centralwidget)
        self.label_TelSiteLongitude.setObjectName(_fromUtf8("label_TelSiteLongitude"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelSiteLongitude, 5, 2, 1, 1)
        self.lineEdit_TelAzimuth = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelAzimuth.setObjectName(_fromUtf8("lineEdit_TelAzimuth"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelAzimuth, 12, 1, 1, 1)
        self.lineEdit_SiteLatitude = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_SiteLatitude.setObjectName(_fromUtf8("lineEdit_SiteLatitude"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_SiteLatitude, 6, 1, 1, 1)
        self.lineEdit_TelSiteName = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelSiteName.setObjectName(_fromUtf8("lineEdit_TelSiteName"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelSiteName, 6, 0, 1, 1)
        self.label_TelSiteName = QtGui.QLabel(self.centralwidget)
        self.label_TelSiteName.setObjectName(_fromUtf8("label_TelSiteName"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelSiteName, 5, 0, 1, 1)
        self.lineEdit_TelDate = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelDate.setObjectName(_fromUtf8("lineEdit_TelDate"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelDate, 4, 0, 1, 1)
        self.lineEdit_TelTime = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_TelTime.setObjectName(_fromUtf8("lineEdit_TelTime"))
        self.gridLayout_TescopeInfo.addWidget(self.lineEdit_TelTime, 4, 1, 1, 1)
        self.label_TelDate = QtGui.QLabel(self.centralwidget)
        self.label_TelDate.setObjectName(_fromUtf8("label_TelDate"))
        self.gridLayout_TescopeInfo.addWidget(self.label_TelDate, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_TescopeInfo, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label_SystemTime.setBuddy(self.timeEdit_SetLocalTime)
        self.label_SetTelSiteLatitude.setBuddy(self.spinBox_setSiteLatitudeDegrees)
        self.label_SystemDate.setBuddy(self.dateEdit_SetLocalDate)
        self.label_SetLocation.setBuddy(self.lineEdit_SetLocation)
        self.label_TelTrackingMode.setBuddy(self.comboBox_TrackingMode)
        self.label_SetTelSiteLongitude.setBuddy(self.spinBox_setSiteLongitudeDegrees)
        self.label_Gain.setBuddy(self.spinBox_Gain)
        self.label_Threshold.setBuddy(self.spinBox_Threshold)
        self.label_Exposure.setBuddy(self.doubleSpinBox_Exposure)
        self.label_AvgBrightness.setBuddy(self.lineEdit_Avg_Brightness)
        self.label_FrameCaptured.setBuddy(self.lineEdit_Frame_Captured)
        self.label_pctGoodFrames.setBuddy(self.lineEdit_pct_GoodFrames)
        self.label_TelSiteLatitude.setBuddy(self.lineEdit_SiteLatitude)
        self.label_TelDec.setBuddy(self.lineEdit_TelDEC)
        self.label_TelSlewRate.setBuddy(self.lineEdit_TelSlewRate)
        self.label_TelAltitud.setBuddy(self.lineEdit_TelAltitud)
        self.label_TelTime.setBuddy(self.lineEdit_TelTime)
        self.label_TelAligment.setBuddy(self.lineEdit_TelAlignment)
        self.label_TelRA.setBuddy(self.lineEdit_TelRA)
        self.label_TelAzimuth.setBuddy(self.lineEdit_TelAzimuth)
        self.label_TelSiteLongitude.setBuddy(self.lineEdit_SiteLongitud)
        self.label_TelSiteName.setBuddy(self.lineEdit_TelSiteName)
        self.label_TelDate.setBuddy(self.lineEdit_TelDate)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_GetTimeDate, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.getTimeDate)
        QtCore.QObject.connect(self.pushButton_SetTelescopeData, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.SetTelescopeData)
        QtCore.QObject.connect(self.pushButton_GetTel_Info, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.GetTelescopeInfo)
        QtCore.QObject.connect(self.pushButton_Park, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.park)
        QtCore.QObject.connect(self.pushButton_StopGoTo, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.halt)
        QtCore.QObject.connect(self.pushButton_UpArrow, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.move_up)
        QtCore.QObject.connect(self.pushButton_UpArrow, QtCore.SIGNAL(_fromUtf8("released()")), MainWindow.stop_up)
        QtCore.QObject.connect(self.pushButton_LeftArrow, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.move_left)
        QtCore.QObject.connect(self.pushButton_LeftArrow, QtCore.SIGNAL(_fromUtf8("released()")), MainWindow.stop_left)
        QtCore.QObject.connect(self.pushButton_RightArrow, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.move_right)
        QtCore.QObject.connect(self.pushButton_RightArrow, QtCore.SIGNAL(_fromUtf8("released()")), MainWindow.stop_right)
        QtCore.QObject.connect(self.pushButton_DownArrow, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.move_down)
        QtCore.QObject.connect(self.pushButton_DownArrow, QtCore.SIGNAL(_fromUtf8("released()")), MainWindow.stop_down)
        QtCore.QObject.connect(self.pushButton_Speed1, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.speed1)
        QtCore.QObject.connect(self.pushButton_Speed2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.speed2)
        QtCore.QObject.connect(self.pushButton_Speed3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.speed3)
        QtCore.QObject.connect(self.pushButton_Speed4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.speed4)
        QtCore.QObject.connect(self.pushButton_Sleep, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.TelSleep)
        QtCore.QObject.connect(self.pushButton_Home, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.go_home)
        QtCore.QObject.connect(self.comboBox_TrackingMode, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), MainWindow.set_mode)
        QtCore.QObject.connect(self.pushButton_Activate_Video, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ActivateVideo)
        QtCore.QObject.connect(self.doubleSpinBox_Exposure, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.set_exposure)
        QtCore.QObject.connect(self.spinBox_Gain, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.set_gain)
        QtCore.QObject.connect(self.spinBox_Threshold, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.set_threshold)
        QtCore.QObject.connect(self.pushButton_AlignTelescope, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.alignTelescope)
        QtCore.QObject.connect(self.radioButton_CopyToFile, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.copyToFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_GetTimeDate, self.comboBox_TrackingMode)
        MainWindow.setTabOrder(self.comboBox_TrackingMode, self.spinBox_setSiteLongitudeDegrees)
        MainWindow.setTabOrder(self.spinBox_setSiteLongitudeDegrees, self.spinBox_setSiteLongitudMinutes)
        MainWindow.setTabOrder(self.spinBox_setSiteLongitudMinutes, self.spinBox_setSiteLatitudeDegrees)
        MainWindow.setTabOrder(self.spinBox_setSiteLatitudeDegrees, self.spinBox_setSiteLatitudeMinutes)
        MainWindow.setTabOrder(self.spinBox_setSiteLatitudeMinutes, self.pushButton_SetTelescopeData)
        MainWindow.setTabOrder(self.pushButton_SetTelescopeData, self.pushButton_GetTel_Info)
        MainWindow.setTabOrder(self.pushButton_GetTel_Info, self.pushButton_Park)
        MainWindow.setTabOrder(self.pushButton_Park, self.pushButton_UpArrow)
        MainWindow.setTabOrder(self.pushButton_UpArrow, self.pushButton_DownArrow)
        MainWindow.setTabOrder(self.pushButton_DownArrow, self.pushButton_LeftArrow)
        MainWindow.setTabOrder(self.pushButton_LeftArrow, self.pushButton_Speed4)
        MainWindow.setTabOrder(self.pushButton_Speed4, self.pushButton_RightArrow)
        MainWindow.setTabOrder(self.pushButton_RightArrow, self.pushButton_Home)
        MainWindow.setTabOrder(self.pushButton_Home, self.lineEdit_TelSiteName)
        MainWindow.setTabOrder(self.lineEdit_TelSiteName, self.pushButton_Speed3)
        MainWindow.setTabOrder(self.pushButton_Speed3, self.pushButton_StopGoTo)
        MainWindow.setTabOrder(self.pushButton_StopGoTo, self.lineEdit_TelDEC)
        MainWindow.setTabOrder(self.lineEdit_TelDEC, self.lineEdit_TelSlewRate)
        MainWindow.setTabOrder(self.lineEdit_TelSlewRate, self.lineEdit_TelRA)
        MainWindow.setTabOrder(self.lineEdit_TelRA, self.lineEdit_TelAltitud)
        MainWindow.setTabOrder(self.lineEdit_TelAltitud, self.lineEdit_TelAzimuth)
        MainWindow.setTabOrder(self.lineEdit_TelAzimuth, self.lineEdit_TelAlignment)
        MainWindow.setTabOrder(self.lineEdit_TelAlignment, self.pushButton_Speed1)
        MainWindow.setTabOrder(self.pushButton_Speed1, self.lineEdit_SiteLatitude)
        MainWindow.setTabOrder(self.lineEdit_SiteLatitude, self.lineEdit_SiteLongitud)
        MainWindow.setTabOrder(self.lineEdit_SiteLongitud, self.pushButton_Sleep)
        MainWindow.setTabOrder(self.pushButton_Sleep, self.lineEdit_SetLocation)
        MainWindow.setTabOrder(self.lineEdit_SetLocation, self.dateEdit_SetLocalDate)
        MainWindow.setTabOrder(self.dateEdit_SetLocalDate, self.timeEdit_SetLocalTime)
        MainWindow.setTabOrder(self.timeEdit_SetLocalTime, self.pushButton_Speed2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Telescope Control System", None))
        self.pushButton_Speed2.setText(_translate("MainWindow", "2", None))
        self.pushButton_Home.setText(_translate("MainWindow", "Home", None))
        self.pushButton_Speed4.setText(_translate("MainWindow", "4", None))
        self.pushButton_Speed1.setText(_translate("MainWindow", "1", None))
        self.pushButton_Speed3.setText(_translate("MainWindow", "3", None))
        self.pushButton_Park.setText(_translate("MainWindow", "Park", None))
        self.pushButton_Sleep.setText(_translate("MainWindow", "Sleep", None))
        self.pushButton_StopGoTo.setText(_translate("MainWindow", "Stop GoTo", None))
        self.pushButton_AlignTelescope.setText(_translate("MainWindow", "Init Alignment", None))
        self.spinBox_setSiteLongitudeDegrees.setSuffix(_translate("MainWindow", " Deg", None))
        self.label_SystemTime.setText(_translate("MainWindow", "Local time", None))
        self.label_SetTelSiteLatitude.setText(_translate("MainWindow", "Site Latitude", None))
        self.spinBox_setSiteLatitudeMinutes.setSuffix(_translate("MainWindow", " Min", None))
        self.label_SystemDate.setText(_translate("MainWindow", "Local Date", None))
        self.spinBox_setSiteLatitudeDegrees.setSuffix(_translate("MainWindow", " Deg", None))
        self.spinBox_setSiteLongitudMinutes.setSuffix(_translate("MainWindow", " Min", None))
        self.label_SetLocation.setText(_translate("MainWindow", "Location Name", None))
        self.comboBox_TrackingMode.setItemText(0, _translate("MainWindow", "AltAz Mode", None))
        self.comboBox_TrackingMode.setItemText(1, _translate("MainWindow", "Land Mode", None))
        self.comboBox_TrackingMode.setItemText(2, _translate("MainWindow", "Polar Mode", None))
        self.label_TelTrackingMode.setText(_translate("MainWindow", "Mode", None))
        self.label_SetTelSiteLongitude.setText(_translate("MainWindow", "Site Longitud", None))
        self.pushButton_GetTimeDate.setText(_translate("MainWindow", "Get Time&Date", None))
        self.pushButton_SetTelescopeData.setText(_translate("MainWindow", "Set", None))
        self.lineEdit_FileName.setText(_translate("MainWindow", "C:\\Users\\Papa\\Desktop\\Images\\Capture", None))
        self.label_VideoCapture.setText(_translate("MainWindow", "Video Capture", None))
        self.doubleSpinBox_Exposure.setSuffix(_translate("MainWindow", " seg", None))
        self.label_Gain.setText(_translate("MainWindow", "Gain", None))
        self.label_Threshold.setText(_translate("MainWindow", "Threshold", None))
        self.label_Exposure.setText(_translate("MainWindow", "Exposure", None))
        self.label_AvgBrightness.setText(_translate("MainWindow", "Avg. Brightness", None))
        self.label_FrameCaptured.setText(_translate("MainWindow", "Frame Captured", None))
        self.label_pctGoodFrames.setText(_translate("MainWindow", "% Good Frames", None))
        self.pushButton_Activate_Video.setText(_translate("MainWindow", "Activate Video", None))
        self.radioButton_CopyToFile.setText(_translate("MainWindow", "Send Img. to File", None))
        self.label_TelSiteLatitude.setText(_translate("MainWindow", "Site Latitude", None))
        self.label_TelescopeInfo.setText(_translate("MainWindow", "Telescope Info", None))
        self.label_TelDec.setText(_translate("MainWindow", "DEC", None))
        self.label_TelSlewRate.setText(_translate("MainWindow", "Slew Rate", None))
        self.label_TelAltitud.setText(_translate("MainWindow", "Altitud", None))
        self.label_TelTime.setText(_translate("MainWindow", "Time", None))
        self.label_TelAligment.setText(_translate("MainWindow", "Aligment", None))
        self.pushButton_GetTel_Info.setText(_translate("MainWindow", "Get Telescope Info", None))
        self.label_TelRA.setText(_translate("MainWindow", "RA", None))
        self.label_TelAzimuth.setText(_translate("MainWindow", "Azimuth", None))
        self.label_TelSiteLongitude.setText(_translate("MainWindow", "Site Longitud", None))
        self.label_TelSiteName.setText(_translate("MainWindow", "Site Name", None))
        self.label_TelDate.setText(_translate("MainWindow", "Date", None))

import Icons_rc
