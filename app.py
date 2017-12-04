from flask import Flask, request, render_template
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import os
from dejavu import Dejavu
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
 file = request.files['file']
 filename = secure_filename(file.filename)

 # os.path.join is used so that paths work in every operating system
 file.save(os.path.join("temp",filename))

 # You should use os.path.join here too.

 with open("dejavu.cnf.SAMPLE") as f:
  config = json.load(f)
 djv = Dejavu(config)
 song = djv.recognize(FileRecognizer, "temp/"+filename)
 path = "temp/"+filename
 os.remove(path)
 return "From file we recognized: %s\n" % song

@app.route('/fingerprint')
def fingerprint():
    with open("dejavu.cnf.SAMPLE") as f:
     config = json.load(f)
    djv = Dejavu(config)
    djv.fingerprint_directory("songs", [".mp3"])
    return "Finish"

if __name__ == "__main__":
    app.run(debug=True)
