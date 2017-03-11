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

if __name__ == "__main__":
	app.run(debug=True)


