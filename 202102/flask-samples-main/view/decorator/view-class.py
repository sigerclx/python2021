from flask import Flask, request, views
from functools import wraps
app = Flask(__name__)

def check_login(original_function11):
    @wraps(original_function11)  #保留原始函数 original_function 的属性,即保留url传入的参数
    def decorated_function(*args,**kwargs):
        user = request.args.get("user")
        pwd = request.args.get("pwd")
        if user == 'zhangsan' and pwd =='123':
             return original_function11(*args, **kwargs)
        else:
            return '请先登录'
    return decorated_function

class Page1(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page1'

class Page2(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page2'

app.add_url_rule(rule='/page1', view_func = Page1.as_view('Page1'))
app.add_url_rule(rule='/page2', view_func = Page2.as_view('Page2'))
app.run(debug = True)

