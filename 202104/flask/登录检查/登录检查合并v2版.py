from flask import Flask,request,render_template,views
from functools import wraps

'''
# 用视图类的方式解决
# http://127.0.0.1:5000/page2
# http://127.0.0.1:5000/page2?user=tom
# http://127.0.0.1:5000/page3
# http://127.0.0.1:5000/page3?user=jacky
# page3 登录检查也继承了
'''

app = Flask(__name__)

def check_login(func):
    @wraps(func)
    def check(*args,**kwargs):
        user =  request.args.get("user")
        if user  and user =='jacky':
            return func(*args,**kwargs)
        else:
            return "请先登录"

    return check


class Page2(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return "page2"

class Page3(Page2):
    #decorators =  [check_login]
    # 登录检查也被继承了
    def dispatch_request(self):
        return 'page3 继承page2'

app.add_url_rule("/page2",view_func=Page2.as_view("page2"))
app.add_url_rule("/page3",view_func=Page3.as_view("page3"))
app.run(debug=True)


