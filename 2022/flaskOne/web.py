# 运行指令：
# flaskOne>set FLASK_APP=web.py
# flaskOne>flask run
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(debug=True,port=5003)