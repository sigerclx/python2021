# from flask_restful import Resource,reqparse
# from db_restful import db
# from db_restful.model.user import User as UserModel
#
# class Login(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument(
#         'password', type=str, required=True, help='{error_msg}'  # 'password required'
#     )
#
#     parser.add_argument(
#         'username', type=str, required=True, help='require username'  # 'username required'
#     )
#
#     def post(self):
#         data = Login.parser.parse_args()
#         user = db.session.query(UserModel).filter(UserModel.username == data['username']).first()
#         if user:
#             if not user.check_password(data['password']):
#                 return {'message': 'user or password error'},201
#             else:
#                 return {
#                            'message': 'login success',
#                            'token': user.generate_token()
#                        }
#         else:
#             {
#                 'message': 'user or password error'
#             }
#
#         user = UserModel(
#             username=username,
#             email=data['email']
#         )
#         user.set_password(data['password'])
#         db.session.add(user)
#         db.session.commit()
#         return {'message': 'user added'}, 201
#
