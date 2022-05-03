# 运行指令：
# flaskOne>set FLASK_APP=web.py
# flaskOne>flask run
from app import app

if __name__ == '__main__':
    app.run(debug=True,port=5003)
