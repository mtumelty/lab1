#!/usr/bin/python

import serial

s = serial.Serial("/dev/ttyACM0")

while(True):
	l = s.readline()
	print l.rstrip().split(",")
	
