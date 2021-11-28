from db_restful import db

class Base(db.Model):
    __abstract__ = True   # 防止系统误认为是一个table，加上这个类就是一个抽象的正常类
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def as_dict(self):
        return {c.name : getattr(self,c.name) for c in self.__table__.columns}