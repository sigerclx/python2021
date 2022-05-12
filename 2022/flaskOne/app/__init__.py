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

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = '请先登录.'
bootstrap = Bootstrap()

basevalues = BaseValue()
# 全局变量（多个请求之间共享的变量，每个请求都可以对其进行修改。）
baseDict = {}
baseDict['dbs'] = basevalues.dbs
baseDict['tables'] = basevalues.tables
baseDict['reimbursement'] = basevalues.reimbursement

def create_app(config_class=Config):
    app = Flask(__name__)
    # 获取loginform的加密密钥，从config.py中取得
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    # 登录插件 #  pip install flask-login login插件，插件都是类似的安装方式
    login.init_app(app)
    # Flask-Login提供了一个非常有用的功能——强制用户在查看应用的特定页面之前登录。 如果未登录的用户
    # 尝试查看受保护的页面，Flask-Login将自动将用户重定向到登录表单，并且只有在登录成功后才重定向到
    # 用户想查看的页面。为了实现这个功能，Flask-Login需要知道哪个视图函数用于处理登录认证。
    # 'login'值是登录视图函数（endpoint）名，换句话说该名称可用于url_for()函数的参数并返回对应的URL
    # '''
    # bootstrap插件
    bootstrap.init_app(app)

    # 多组蓝图，每个蓝图相当于独立模块
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    from app.home import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/home')

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

    app.run(host='0.0.0.0', debug=True, port=5003)
    return app

from app import  models