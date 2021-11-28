from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)
user_list =[]


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

class Helloworld(Resource):
    def get(self):
        return user_list

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True, help='{error_msg}' #'password required'
    )

    def get(self,username):
        '''
        get user infomation detail
        :param username:
        :return:
        '''


        for user in user_list:
            if user['username']== username:
                return user
        return {'message':'user not found'},404

    def post(self,username):
        '''
        add user
        :param username:
        :return:
        '''


        data = User.parser.parse_args()

        user  ={
            'username':username,
            'password':data.get('password')
        }

        for u in user_list:
            if u['username']==username:
                return  {'message': 'user already exist'}, 200
        user_list.append(user)
        return {'message': 'user added'}, 201



    def delete(self,username):
        '''
        delete user
        :param username:
        :return:
        '''
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user

        if user_find:
            user_list.remove(user_find)
            return  {'message':'user deleted'}
        else:
            return  {'message':'user not found'},200

    def put(self,username):
        '''
        update user info
        :param username:
        :return:
        '''

        user_find = None
        for user in user_list:
            if user['username']==username:
                user_find = user
            if user_find:
                data = User.parser.parse_args()
                user_list.remove(user_find)
                user_find['password'] =data.get('password')
                user_list.append(user_find)
                return user_find
            else:
                return  {'message':'user not found'},404

api.add_resource(Helloworld,'/')
api.add_resource(User,'/user/<string:username>')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True ,port = 5000)