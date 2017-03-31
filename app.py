from flask import Flask, render_template,jsonify
import random
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('home.html')

#example of using rest api for use with our website
@app.route("/api/iname")
def iname():
    #idealy this will run some other scripts and return the name of item kept in iDabba
    #returns json data
    names= ['banana','orange','garlic','apple','potato']
    x = names[random.randint(0,len(names)-1)]
    return jsonify({'objectName':x})

@app.route("/api/temp/<string:data>")
def tempDataLoad(data):
	print data
	fo = open("dataLog.txt","a+")
	fo.write(data)
	fo.write('\n')
	fo.close()
	return "recieved"

@app.route("/api/getrd")
def returnData():
	fo = open("dataLog.txt")
	y = ""
	for x in fo:
		y = x
	return y
# @app.route("/api/humidity/<string:data>") 
# def humidityDataLoad(data):
# 	print data
# 	return "recieved"

# @app.route("/api/rfid/<string:data>")
# def rfidDataLoad(data):
# 	print data
# 	return "recieved"

# @app.route("/api/weight/<string:data>")
# def weightDataLoad(data):
# 	print data
# 	return "recieved"


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080) 
	# ,debug=True


