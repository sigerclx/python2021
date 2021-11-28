# python -m pip install jwt
# python -m pip install pyjwt
# 上面2个jwt都要安装，jwt才能使用，否则会出现 jwt 没有 encode属性，或者没有ExpiredSignatureError属性
import jwt


from flask_restful import Resource,reqparse
from flask import request,current_app
from flask_jwt import  jwt_required

from db_restful import db
from db_restful.model.user import User as UserModel
#user_list=[]

def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s,(int,str)):
            raise Exception('password format error')
        s = str(s)
        if len(s)>=min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)
    return validate

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True, help='{error_msg}' #'password required'
    )

    parser.add_argument(
        'email', type=str, required=True, help='require email'  # 'email required'
    )

    def get(self,username):
        '''
        get user infomation detail
        :param username:
        :return:
        '''
        user = db.session.query(UserModel).filter(UserModel.username==username).first()
        if user:
            return user.as_dict()
        return {'message':'user not found'},404

    def post(self,username):
        '''
        add user
        :param username:
        :return:
        '''
        data = User.parser.parse_args()
        print(data)
        user = db.session.query(UserModel).filter(UserModel.username==username).first()
        if user:
            return  {'message': 'user already exist'}, 200
        user = UserModel(
            username= username,
            email = data['email']
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return user.as_dict(),201  #{'message': 'user added'}, 201

    def delete(self,username):
        '''
        delete user
        :param username:
        :return:
        '''
        user = db.session.query(UserModel).filter(UserModel.username == username).first()
        if user:
            user.delete()
            return  {'message':'user deleted'}
        else:
            return  {'message':'user not found'},200

    def put(self,username):
        '''
        update user info
        :param username:
        :return:
        '''

        user = db.session.query(UserModel).filter(UserModel.username == username).first()
        if user:
            data = User.parser.parse_args()
            user.set_password(data["password"])
            db.session.commit()
            return user.as_dict(),200
        else:
            return  {'message':'user not found'},404


class UserList(Resource):
    @jwt_required() # token的认证
    def get(self):
        # token = request.headers.get("Authorization")
        # try:
        #     jwt.decode(
        #         token,
        #         current_app.config.get('SECRET_KEY'),
        #         algorithms='HS256'
        #     )
        #
        # except jwt.ExpiredSignatureError:
        #     return {'message': 'Expired token'}
        #
        # except jwt.InvalidTokenError:
        #     return {'message': 'Invalid token'}

        users = db.session.query(UserModel).all()
        return [u.as_dict() for u in users]