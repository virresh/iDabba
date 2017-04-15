import numpy as np
import cv2
import httplib, urllib, base64, json
import os
import sift
import haar

VIDEO_SRC = 0
MIN_MATCH_COUNT = 20

def getImageFromCam():
	cap = cv2.VideoCapture(VIDEO_SRC)
	ret, frame = cap.read()
	cap.release()
	return frame

def getFromAPI():
	#get object data from Microsoft Computer Vision API
	o = getImageFromCam()
	cv2.imwrite("apiIm.jpg",o)
	headers = {
		# Request headers. The key below is our subscription key for the API.
		'Content-Type': 'application/octet-stream',
		'Ocp-Apim-Subscription-Key': '6f4e3f9a67eb4e09981bc4aa9f8dcd97',
	}

	params = urllib.urlencode({
		# Request parameters. All of them are optional.
		'visualFeatures': 'Categories',
		# 'details': 'Celebrities',
		'language': 'en',
	})	

	pathToFileInDisk = r'apiIm.jpg'
	with open( pathToFileInDisk, 'rb' ) as f:
		data = f.read()

	body = str(data) #"{'url':'https://urltoimage.com/image.jpg'}"
	reply = "None"
	try:
		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/vision/v1.0/describe?%s" % params, body, headers)
		response = conn.getresponse()
		reply = response.read()
		conn.close()
	except Exception as e:
		# print("[Errno {0}] {1}".format(e.errno, e.strerror))
		print(e)

	wordlist = []
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	filename = os.path.join(fileDir, 'nameList')
	file = open(filename,"r")
	for lines in file:
		wordlist.append(lines.strip('\n'))

	r = json.loads(reply)
	for word in r["description"]["tags"]:
		if (str(word) in wordlist):
			return word
	return r["description"]["captions"][0]["text"]

def getD():
	wordlist = []
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	filename = os.path.join(fileDir, 'nameList')
	file = open(filename,"r")
	for lines in file:
		wordlist.append(lines.strip('\n'))

	return str(wordlist)

def getViaSift():
	img2 = cv2.cvtColor(getImageFromCam(), cv2.COLOR_BGR2GRAY)        # trainImage

	# Initiate SIFT detector
	sift = cv2.xfeatures2d.SIFT_create()

	# find the keypoints and descriptors with SIFT
	kp2, des2 = sift.detectAndCompute(img2,None)

	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)

	flann = cv2.FlannBasedMatcher(index_params, search_params)

	mypath = 'imdata'
	fileList = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f))]
	
	for k in fileList:
		img1 = cv2.imread(mypath+"/"+k,0)          # queryImage
		kp1, des1 = sift.detectAndCompute(img1,None)

		matches = flann.knnMatch(des1,des2,k=2)
		# store all the good matches as per Lowe's ratio test.
		good = []
		for m,n in matches:
			if m.distance < 0.7*n.distance:
				good.append(m)
		if len(good)>MIN_MATCH_COUNT:
			return k.split('_')[0]

	return "Cannot Detect"


def getViaHaar():
	im = getImageFromCam()
	y = haar.getItemH(im)
	return y