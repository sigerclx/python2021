from flask import Flask
from flask_restful import Api
from resource.user import User,UserList
from resource.hello import Helloworld
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)



api.add_resource(Helloworld,'/')
api.add_resource(UserList,'/userlist')
api.add_resource(User,'/user/<string:username>')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True ,port = 5000)