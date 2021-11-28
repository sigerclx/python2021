from db_restful import db

class Demo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
