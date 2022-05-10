from flask import Flask
from config import Config
from app.share import BaseValue
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os
import logging
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# 获取loginform的加密密钥，从config.py中取得
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#  pip install flask-login login插件，插件都是类似的安装方式
login = LoginManager(app)
'''
Flask-Login提供了一个非常有用的功能——强制用户在查看应用的特定页面之前登录。 如果未登录的用户
尝试查看受保护的页面，Flask-Login将自动将用户重定向到登录表单，并且只有在登录成功后才重定向到
用户想查看的页面。为了实现这个功能，Flask-Login需要知道哪个视图函数用于处理登录认证。
'login'值是登录视图函数（endpoint）名，换句话说该名称可用于url_for()函数的参数并返回对应的URL
'''
login.login_view = 'auth.login'

basevalues = BaseValue()
# 全局变量（多个请求之间共享的变量，每个请求都可以对其进行修改。）
baseDict={}
baseDict['dbs']=basevalues.dbs
baseDict['tables']=basevalues.tables
baseDict['reimbursement'] = basevalues.reimbursement

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app.main import bp as main_bp
app.register_blueprint(main_bp, url_prefix='/main')

from app import  models ,routes

if not app.debug:
    # 给系统增加日志功能

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('jacky purchase startup')