#!/usr/bin/env python

'''
Detects item from live web-camera using haar cascades
Does not show the live-stream. Only reports back the result
'''

from os import listdir
from os.path import isfile, join
import numpy as np
import cv2

# local modules
from video import create_capture



def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

def draw_rects(img, rects, color):
	for x1, y1, x2, y2 in rects:
		cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
			
	#get the list of classifiers available :
	mypath = 'classifiers'
	fileList = [ f for f in listdir(mypath) if isfile(join(mypath,f))]

	video_src=0; #this is the default video source available
	cam = create_capture(video_src) #capture that video source

	objectInBox = 'None'
	l = []
	#iterate over every damn classifier and run it on the captured picture. whatever it results in, return that item
	for i in range(10):
		#fetch the correct cascade
		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)
		rects = []
		t = []
		for x in fileList:
			cascade_fn = "classifiers/"+x
			cascade = cv2.CascadeClassifier(cascade_fn)
			#try this classifier for the next 5 frames
			rects = detect(gray, cascade)
			if(len(rects) != 0):
				#rects is not empty, an object spotted
				t.append(x)
		if(len(rects)!=0):
			objectInBox = x
			# break;
		if(len(t)!=0):
			i = len(t)/2
			l.append(t[i])
			print t
	j = len(l)/2
	objectInBox = l[j]
	print l
	print objectInBox


