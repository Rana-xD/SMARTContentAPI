from flask import Flask, request, render_template,jsonify
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from werkzeug import secure_filename
import json
import requests
import os
from dejavu import Dejavu
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html',code=0)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
 result = ""
 if request.method == 'POST':
   print request
   if 'file' not in request.files:
     print('No file part')
   file = request.files['file']
   if file.filename == '':
     print('No selected file')
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
 title = song["song_name"].replace('_',' ')
 confidence = song["confidence"]
 if(confidence<50):
   result = {'title' : "Unknown Song"}
 else:
   result = {'title' : title}
 infoJson = requests.get('http://128.199.181.183:5000/?title='+title).json()
#  info = json.loads(infoJson.text)
#  print infoJson
#  print info
 return infoJson

@app.route('/fingerprint',methods = ['GET','POST'])
def fingerprint():
  uploaded_files = request.files.getlist("files")
  for file in uploaded_files:
    filename = secure_filename(file.filename)
    file.save(os.path.join("song",filename))
  print "Mean aii"
  with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)
  djv = Dejavu(config)
  djv.fingerprint_directory("song", [".mp3"])
  for file in uploaded_files:
    filename = secure_filename(file.filename)
    path = "song/"+filename
    os.remove(path)
  print "Delete aii"
  return render_template('index.html',code=1)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
