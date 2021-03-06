#!/usr/bin/python

import serial
import pygame
from pygame.locals import *
import sys
import time

s = serial.Serial("/dev/ttyACM0")
l = 0
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('LED mirror')

while(True):
	l = s.readline()
	COLOR = l.rstrip().split(",")
	try:
		try:
			COLOR_R = int(COLOR[0])
			COLOR_G = int(COLOR[1])
			COLOR_B = int(COLOR[2])
			print COLOR
			DISPLAYSURF.fill((COLOR_R, COLOR_G, COLOR_B))
	
	
			pygame.display.update()
		except IndexError:
			print('IndexPASS')

	except ValueError:
		print("ValuePASS")
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
