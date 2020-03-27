from app import db
from datetime import datetime
class Pressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    pulse = db.Column(db.Integer, nullable=False)
    hour = db.Column(db.Integer,nullable=False)
    minute = db.Column(db.Integer,nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.idr


class Medicine_schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    about = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    interval = db.Column(db.Integer, nullable=False)
    recommendations = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.idr
