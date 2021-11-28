from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'jacky'
password = 'a1b2/a'
database = 'jingyou'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tree(db.Model):
    __tablename__ = 'A_tree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    parentid = db.Column(db.Integer)
    jine = db.Column(db.Float)

    def dump(self):
        print(self.id, self.name, self.parentid,self.jine)

trees = Tree.query.all()
for tree in trees:
    print(tree.id, tree.name, tree.parentid,tree.jine)