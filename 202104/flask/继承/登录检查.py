from flask import Flask,request,render_template
from functools import wraps

app = Flask(__name__)

def check_login(func):
    @wraps(func)
    def check(*args ,**kwargs):
        user = request.args.get("user")
        if user and user =='jacky':
            return True
        else:
            return "请先登录"
    return check

@app.route('/page1')
@check_login
def page1():
    return "page1"


if __name__ == '__main__':
    app.run(debug=True)