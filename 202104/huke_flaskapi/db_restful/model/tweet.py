from sqlalchemy import ForeignKey,func
from db_restful import db
from db_restful.model.base import Base
# windows10 : cmd ： huke_flaskapi>set FLASK_APP=db_restful
# mac terminal : huke_flaskapi>.flaskenv 有此文件即可
'''
每个人发表的blog的表
'''
# token的认证
class Tweet(Base):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,ForeignKey('user.id'))
    body = db.Column(db.String(140))
    created_at = db.Column(db.DateTime,server_default=func.now())
    def __repr__(self):
        return "user_id={},tweet={}".format(
            self.user_id,self.body
        )

    def as_dict(self):
        t ={c.name : getattr(self,c.name) for c in self.__table__.columns}
        t['created_at'] = t['created_at'].isoformat()
        return t
