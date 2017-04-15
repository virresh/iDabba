#!/usr/bin/env python

'''
pen detection from live web-camera using haar cascades

'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

# local modules
from video import create_capture
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
    # import sys, getopt
    print("Use escape key to exit !!!\nAll code based on openCV samples")
    video_src=0;
    cascade_fn = "classifiers/banana_classifier.xml"
    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = create_capture(video_src)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        #print(str(rects))
        draw_rects(vis, rects, (0, 255, 0))
        dt = clock() - t
        cv2.imshow('Pen detect', vis)
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
