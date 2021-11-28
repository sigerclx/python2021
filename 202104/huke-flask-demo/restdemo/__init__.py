from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
'''
项目地址（虎课网教程源码地址）
- https://github.com/udemy-course/flask-rest-demo
- 只加了本地运行的代码
- 数据库从自己制作的版本生成的
- windows dos窗口下: set FLASK_APP = restdemo 
- flask db init
- flask db migrate
- flask db upgrade
'''

db = SQLAlchemy()
migrate = Migrate()

from restdemo.model.user import User as UserModel
from restdemo.resource.user import User, UserList
from restdemo.resource.hello import Helloworld
from restdemo.resource.tweet import Tweet
from restdemo.config import app_config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)


def create_app(config_name='development'):

    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')
    api.add_resource(Tweet, '/tweet/<string:username>')
    return app

# - 只加了本地运行的代码如下
if __name__ == '__main__':
    app= create_app()
    app.run(host = '127.0.0.1', debug=True ,port = 5000)