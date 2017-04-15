from flask import Flask, render_template,jsonify
import random
from objD import auxF
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

#example of using rest api for use with our website
@app.route("/api/iname")
def iname():
    #This will run some other scripts and return the name of item kept in iDabba
    # return auxF.getFromAPI()	#use this to get information from the microsoft API server. Internet connection needed.
    # return auxF.getViaHaar()	#use this to get information using our own generated haar cascades. No internet Needed.
    return auxF.getViaSift()	#use this to get information using sift Features calculated on the go. No internet Needed.
    # return auxF.test()

@app.route("/api/store/<string:data>")
def DataLoad(data):
	#stores the data into the log file
	fo = open("dataLog.txt","a+")
	fo.write(data)
	fo.write('\n')
	fo.close()
	return "recieved"

@app.route("/api/getrd")
def returnData():
	#returns data about object in iDabba
	fo = open("dataLog.txt")
	y = ""
	for x in fo:
		y = x
	p = y.replace("\n","_")
	z = p.split("_");
	
	d = {'objectName':iname(),'temp':z[0],'humidity':z[1],'weight':z[2],'rfid':z[3]}
	return jsonify(d)

@app.route("/api/click/<string:fname>")
def clickP(fname):
	#Clicks a picture of object inside iDabba and saves it as the given name
	im = auxF.getImageFromCam()
	auxF.cv2.imwrite('imdata/'+fname+'.jpg',im)
	return "Done"

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080) 
	# ,debug=True


