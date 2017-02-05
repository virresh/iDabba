#!/usr/bin/env python

'''
banana detection on hardcoded images using haar cascades
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

# local modules
from common import clock, draw_str


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
	print("Use escape key to exit !!!\nAll code based on openCV samples")
	cascade_fn = "classifiers/banana_classifier.xml"
	cascade = cv2.CascadeClassifier(cascade_fn)
	img = cv2.imread('bananas/bananasf5.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)

	t = clock()
	rects = detect(gray, cascade)
	vis = img.copy()
	draw_rects(vis, rects, (0, 255, 0))
	cv2.imshow('bananadetect', vis)
	while(1):
		k = cv2.waitKey(0)
		if(k == 27):
			break
	cv2.destroyAllWindows()
