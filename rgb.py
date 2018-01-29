#!/usr/bin/python

import serial
import pygame, sys

s = serial.Serial("/dev/ttyACM0")
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('LED mirror')

while(True):
	l = s.readline()
	print l.rstrip().split(",")
	
	'''for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()'''
	pygame.display.update()
