from app import db



class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    course = db.Column(db.String(30))
    price = db.Column(db.String(7))
    description = db.Column(db.String(240))
    timestamp = db.Column(db.DateTime)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Item %r>' % (self.title)