from main import db
from datetime import datetime

# model for DATABASE

class Booking_date(db.Model):

    __tablename__ = 'booking_date'

    id = db.Column(db.Integer, primary_key=True)
    book_on = db.Column(db.Date)
    book_by = db.Column(db.String)

    time = db.relationship('Booking_time')

    def __init__(self, book_on, book_by):
        self.book_on = book_on
        self.book_by = book_by

    def __repr__(self):
        return f"book_on: {self.book_on}"

class Booking_time(db.Model):

    __tablename__ = 'booking_time'

    id = db.Column(db.Integer, primary_key=True)
    book_on_id = db.Column(db.Integer, db.ForeignKey('booking_date.id'))
    book_from = db.Column(db.Integer)
    book_to = db.Column(db.Integer)

    def __init__(self, book_on_id, book_from, book_to):
        self.book_on_id = book_on_id
        self.book_from = book_from
        self.book_to = book_to
