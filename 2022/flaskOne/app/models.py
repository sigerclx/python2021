from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #User类有一个新的posts字段，用db.relationship初始化。这不是实际的数据库字段，
    # 而是用户和其动态之间关系的高级视图，因此它不在数据库图表中。对于一对多关系，
    # db.relationship字段通常在“一”的这边定义，并用作访问“多”的便捷方式。因此，
    # 如果我有一个用户实例u，表达式u.posts将运行一个数据库查询，返回该用户发表过的所有动态。
    # db.relationship的第一个参数表示代表关系“多”的类。 backref参数定义了代表“多”的类的实例
    # 反向调用“一”的时候的属性名称。这将会为用户动态添加一个属性post.author，调用它将返回给该用户动态
    # 的用户实例。 lazy参数定义了这种关系调用的数据库查询是如何执行的
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)



    def __repr__(self):
        # 调试中使用返回对象数据
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




class Post(db.Model):
    # 新的“Post”类表示用户发表的动态。 timestamp字段将被编入索引，
    # 如果你想按时间顺序检索用户动态，这将非常有用。 我还为其添加了一个default参数，
    # 并传入了datetime.utcnow函数。 当你将一个函数作为默认值传入后，SQLAlchemy会将
    # 该字段设置为调用该函数的值（请注意，在utcnow之后我没有包含()，所以我传递函数本身
    # ，而不是调用它的结果）。 通常，在服务应用中使用UTC日期和时间是推荐做法。 这可以确保
    # 你使用统一的时间戳，无论用户位于何处，这些时间戳会在显示时转换为用户的当地时间。

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Reimbursement(db.Model):
    # 新的“Post”类表示用户发表的动态。 timestamp字段将被编入索引，
    # 如果你想按时间顺序检索用户动态，这将非常有用。 我还为其添加了一个default参数，
    # 并传入了datetime.utcnow函数。 当你将一个函数作为默认值传入后，SQLAlchemy会将
    # 该字段设置为调用该函数的值（请注意，在utcnow之后我没有包含()，所以我传递函数本身
    # ，而不是调用它的结果）。 通常，在服务应用中使用UTC日期和时间是推荐做法。 这可以确保
    # 你使用统一的时间戳，无论用户位于何处，这些时间戳会在显示时转换为用户的当地时间。

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    source = db.Column(db.String(10))
    name = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    total = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Reimbursement {}>'.format(self.source)