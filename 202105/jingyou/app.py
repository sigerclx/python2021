# app.py

from functools import wraps
from flask import Flask, request, render_template, redirect, url_for, flash, session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/oil.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
app.secret_key = '123'

db = SQLAlchemy(app)

############################################
# 数据库
############################################
from jingyou.model.User import User
from model.Oil import Oil



############################################
# 辅助函数、装饰器
############################################

# 登录检验（用户名、密码验证）
def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password)).first()
    if user:
        return True
    else:
        return False


# 注册检验（用户名、邮箱验证）
def valid_regist(username, email):
    user = User.query.filter(or_(User.username == username, User.email == email)).first()
    if user:
        return False
    else:
        return True


# 登录
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # if g.user:
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login', next=request.url))  #

    return wrapper

# 1.主页
@app.route('/')
def home():
    return render_template('home.html', username=session.get('username'))


# 2.登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("成功登录！")
            session['username'] = request.form.get('username')
            return redirect(url_for('home'))
        else:
            error = '错误的用户名或密码！'

    return render_template('login.html', error=error)


# 3.注销
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


# 4.注册
@app.route('/regist', methods=['GET', 'POST'])
def regist():
    error = None
    if request.method == 'POST':
        if request.form['password1'] != request.form['password2']:
            error = '两次密码不相同！'
        elif valid_regist(request.form['username'], request.form['email']):
            user = User(username=request.form['username'], password=request.form['password1'],
                        email=request.form['email'])
            db.session.add(user)
            db.session.commit()

            flash("成功注册！")
            return redirect(url_for('login'))
        else:
            error = '该用户名或邮箱已被注册！'

    return render_template('regist.html', error=error)


# 5.个人中心
@app.route('/panel')
@login_required
def panel():
    username = session.get('username')
    user = User.query.filter(User.username == username).first()
    return render_template("panel.html", user=user)



if __name__ == '__main__':
    app.run(debug=True,port=5003)