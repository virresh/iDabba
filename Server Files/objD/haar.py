import os
import numpy as np
import cv2

def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

def draw_rects(img, rects, color):
	for x1, y1, x2, y2 in rects:
		cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


def getItemH(img):	

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)

	mypath = 'classifiers'
	fileList = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f))]
	
	objectInBox = 'None'
	#iterate over every damn classifier and run it on the captured picture. whatever it results in, return that item
	rects = []
	t = []
	for x in fileList:
		cascade_fn = "classifiers/"+x 	#fetch the correct cascade
		cascade = cv2.CascadeClassifier(cascade_fn)
		#try this classifier
		rects = detect(gray, cascade)
		if(len(rects) != 0):
			#rects is not empty, an object spotted
			t.append(x.split('_')[0])
		
	if(len(t)!=0):
		i = len(t)/2
		objectInBox = t[i]
	else:
		objectInBox = "Cannot Detect"
	return objectInBox