#!/usr/bin/python3
from flask import Flask, render_template, request, send_from_directory,jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    entries = os.listdir('./upload')
    return render_template('index.html', entries = entries)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    # data  = request.get_json()
    # print(data)
    path = os.path.join('./upload', f.filename)
    f.save(path)
    return jsonify({'message':'file is uploaded !'})
    # return render_template('upload.html')

@app.route('/senddata', methods=['POST'])
def senddata():
    data  = request.get_json()
    print(data)
    return jsonify({'message':'data is got !'})

# 本语句可以让文件被访问下载
@app.route('/files/<filename>')
def files(filename):
    return send_from_directory('./upload', filename, as_attachment=True)

app.run(debug = True)
