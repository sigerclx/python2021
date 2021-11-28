from db_restful import db
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.orm import relationship
from datetime import datetime,timedelta
from flask import current_app
import jwt
from db_restful.model.base import Base

# windows10 : cmd ： huke_flaskapi>set FLASK_APP=db_restful
# mac terminal : huke_flaskapi>.flaskenv 有此文件即可
# flask db migrate ，flask db upgrade

class User(Base):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64),unique=True)

    tweet = relationship('Tweet')  # 通过User.tweet的找到关联表的关联记录

    def __repr__(self):
        return "id={},username={},email={}".format(self.id,self.username,self.email)



    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)



    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()

    @staticmethod
    def authenticate(username,password):
        user = db.session.query(User).filter(
            User.username == username
        ).first()
        if user:
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user =  db.session.query(User).filter(
            User.id == user_id
        ).first()
        return user

    # def generate_token(self):
    #     try:
    #         payload = {
    #             'exp':datetime.utcnow()+timedelta(minutes=5),
    #             'iat':datetime.utcnow(),
    #             'sub':self.username
    #         }
    #
    #         jwt_token = jwt.encode(payload,current_app.config.get('SECRET_KEY'),algorithm='HS256')
    #         return jwt_token
    #     except Exception as e:
    #         return str(e)