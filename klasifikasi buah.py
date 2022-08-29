import os
import random
import cv2
import numpy as np
import time
from copy import deepcopy

Open =np.ones((5,5))
Close =np.ones((20,20))

i=time.strftime("%d-%m-%y_%H-%M-%S")

path = input("Masukkan Path Gambar : " )
citra = cv2.imread(path, cv2.IMREAD_UNCHANGED)
img = cv2.imread(path)


hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

redmask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])

redmask2 = cv2.inRange(hsv, lower_red, upper_red)

redmask=redmask1+redmask2
maskOpen=cv2.morphologyEx(redmask,cv2.MORPH_OPEN,Open)
maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,Close)

maskFinal=maskClose

cnt_r=0
for r in redmask:
	cnt_r=cnt_r+list(r).count(255)
print ("Merah ",cnt_r)

lower_green=np.array([50,50,50])
upper_green=np.array([70,255,255])
greenmask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow('Layer Green:',greenmask)
cnt_g=0
for g in greenmask:
	cnt_g=cnt_g+list(g).count(255)
print ("Hijau ",cnt_g)

lower_yellow=np.array([20,50,50])
upper_yellow=np.array([30,255,255])
yellowmask = cv2.inRange(hsv, lower_yellow, upper_yellow)
cv2.imshow('Layer Kuning:',yellowmask)
cnt_y=0
for y in yellowmask:
	cnt_y=cnt_y+list(y).count(255)
print ("Kuning",cnt_y)

tot_area=cnt_r+cnt_y+cnt_g
rperc=cnt_r/tot_area
yperc=cnt_y/tot_area
gperc=cnt_g/tot_area

glimit=0.5
ylimit=0.8

if gperc>glimit:
	print ("Tomat Belum matang")
	cv2.imshow('Belum matang',img)
else:
	print ("Sudah matang")
	cv2.imshow('Tomat Sudah matang',img)
while True: 
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cv2.waitKey(0)
cv2.destroyAllWindows() 
