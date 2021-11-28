from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

db = SQLAlchemy()
from db_restful.model.user import  User as UserModel
from db_restful.model.tweet import Tweet as TweetModel
from db_restful.resource.user import User,UserList
from db_restful.resource.hello import Helloworld
from db_restful.resource.tweet import Tweet
#from db_restful.resource.auth import Login
from db_restful.config import app_config


jwt = JWT(None,UserModel.authenticate,UserModel.identity)

def create_app(config_name='development'):

    app = Flask(__name__)
    api = Api(app)
    # 连接本地的sqlite数据库，自动按model里的user 和 demo 类生成数据库的表
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migtate = Migrate(app,db)
    jwt.init_app((app))

    api.add_resource(Helloworld,'/')
    api.add_resource(UserList,'/userlist')
    api.add_resource(User,'/user/<string:username>')
    api.add_resource(Tweet,'/tweet/<string:username>')
    return app

if __name__ == '__main__':
    app= create_app()
    app.run(host = '127.0.0.1', debug=True ,port = 5000)