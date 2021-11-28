from flask import Flask,request,render_template,views
from functools import wraps

app = Flask(__name__)

# 用视图函数的方式解决
# 使用 http://127.0.0.1:5000/page1?user=jacky 检查登录


def check_login(func):
    @wraps(func)
    def check(*args ,**kwargs):
        user = request.args.get("user")
        if user and user =='jacky':
            return func(*args, **kwargs)
        else:
            return "请先登录"
    return check

@app.route('/page1')
@check_login
def page1():
    return "page1"


if __name__ == '__main__':
    app.run(debug=True)