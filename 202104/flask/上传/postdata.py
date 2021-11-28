import requests,json
# 本例子是向接收json的API发送json，并获得json返回值
from flask import jsonify
url = 'http://127.0.0.1:5000/senddata'

data1 = {"xxx":"aa"}

# headers = {"content-type":"application/json"}
# response = requests.post(url, json=data1,headers=headers)

response = requests.post(url, json=data1)

json = response.json()
print(response)
