import requests,json
# 本例子是向接收上传文件的API发送文件，并获得返回值
from flask import jsonify
url = 'http://127.0.0.1:5000/upload'
files = {'file': open('121.txt', 'rb')}
data1 = {"xxx":"aa"}

# headers = {"content-type":"application/json"}
# response = requests.post(url, json=data1,headers=headers)
response = requests.post(url, files=files)
json = response.json()
print(response)
