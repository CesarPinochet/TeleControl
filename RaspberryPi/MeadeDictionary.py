# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 07:32:12 2018

@author: d351157
"""
# File with MEADE ETX Command Grammar
# http://www.skymtn.com/mapug-astronomy/ragreiner/lx200CmdSet.html
# http://www.weasner.com/etx/autostar/as_testing.html
# TEL_CMD Dictionary has the following format
# (:MEADE cmd,n_char to receive)
# n_Char to Receive can be a # indicating read until a  # arrives
TEL_CMD = {
# Toggle Precision
'TOGGLE_PRECISION':(':U' ,0),
	#Low - RA displays and messages HH:MM.T sDD*MM
	#High - Dec/Az/El displays and messages HH:MM:SS sDD*MM:SS
	
# Set commands
#Alignment Commands
'START_AUTO_ALIGNMENT':(':Aa',1),
'SET_ALIGNMENT_LAND':(':AL',0),
'SET_ALIGNMENT_POLAR':(':AP',0),
'SET_ALIGNMENT_AltAz':(':AA',0),

# Slew speed commands
'SET_SLEW_CENTER':(':RC',0), # 2nd slowest
'SET_SLEW_GUIDE':(':RG',0),  # Slowest
'SET_SLEW_FIND':(':RM',0),   # 2nd Fastest
'SET_SLEW_FAST':(':RS',0),   # Fastest

# Set target object
'SET_OBJ_ALTITUDE':(':Sa',1), #_CMD:DD*MM#
'SET_OBJ_AZ':(':Sz',1),  # _CMD:DDD*MM#

'SET_OBJ_DECLINATION':(':Sd',1), #_CMD:DD/MM#
'SET_OBJ_RA':(':Sr',1),  # _CMD:HH:MM:T# or HH:MM:SS# Depending on current precision setting

# Site configuration
'SET_SELECT_SITE':('W',0), #_CMD Wx where x is site number  = 1 2 3 or 4
'SET_DEFAULT_TRAKING_RATE':(':TQ',0),
'SET_HANDBOX_DATE':(':SC','#'), #_CMD:MM/DD/YY# NOTE: This CMD returns two strings
'SET_SITE_LONGITUDE':(':Sg',1), #_CMD:DDD*MM# East Longitud should be (360 -  Long) 145 East :> 215 
'SET_SITE_LATITUDE':(':St',1),# _CMD:DD*MM#
 
'SET_LOCAL_TIME':(':SL',1),  # _CMD:HH:MM:SS#
'SET_SITE_NAME':(':SM',1),  #_CMD:Site Name#
'SET_DAYLIGHT_SAVINGS':('SH',0), # _CMD: SHD where D=1 Enable, D=0 Disable 

# Get Information
'ASK_ALIGNMENT':(':GW',3),
'ASK_LOCAL_TIME_12':(':Ga','#'),
'ASK_LOCAL_TIME_24':(':GL','#'),

'ASK_SIDERAL_TIME':(':GS','#'),
'ASK_GMT_HOUR':(':GG','#'),
'ASK_CALENDAR_DATE':(':GC','#'),

'ASK_TEL_ALT':(':GA','#'),
'ASK_TEL_AZ':(':GZ','#'),

'ASK_TEL_DEC':(':GD','#'),
'ASK_TEL_RA':(':GR','#'),

'ASK_OBJ_DEC':(':Gd','#'),
'ASK_OBJ_RA':(':Gr','#'),

'ASK_SITE_LONG':(':Gg','#'),
'ASK_SITE_LAT':(':Gt','#'),
'ASK_SITE_NAME':(':GN','#'),

'ASK_FIND_QUALITY':(':Gq','#'),

# Ask for sensor Information
'ASK_PRECISION':(':P',14),
'ASK_BACKLASH_VALUES':(':GpB','#'),
'ASK_HOME_DATA':(':GpH','#'),
'ASK_SENSOR_OFFSETS':(':GpS','#'),

# Home position commands
'EXE_PARK':(':hP',0),
'EXE_SLEEP':(':hN',0),
'EXE_WAKEUP':('hW',0),
'ASK_HOME_STATUS':(':h?',1),

# Move commands

'EXE_SYNC_CURR':(':CM','#'),  # Looks this can be used to align telescope
'EXE_SYNC_OBJ':(':CL','#'),

'EXE_MOVE_EAST':(':Me',0),
'EXE_MOVE_WEST':(':Mw',0),
'EXE_MOVE_NORTH':(':Mn',0),
'EXE_MOVE_SOUTH':(':Ms',0),
'EXE_GOTO':(':MS','#'), # returns 0<string># = slew is possible, 1<string># = object below horizon, 2<string># object below higher

'EXE_STOP_MOVE_EAST':(':Qe',0),
'EXE_STOP_MOVE_WEST':(':Qw',0),
'EXE_STOP_MOVE_NORTH':(':Qn',0),
'EXE_STOP_MOVE_SOUTH':(':Qs',0),
'EXE_STOP_GOTO':(':Q',0),

'ADDITIONAL_STR':('|','#')
}
#