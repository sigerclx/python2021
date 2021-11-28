from jingyou import db
class Oil(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    englisname = db.Column(db.String(50))
    lading = db.Column(db.String(50))
    func = db.Column(db.String(100))
    def __repr__(self):
        return '<Oil %r>' % self.name