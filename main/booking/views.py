from flask import Blueprint, redirect, render_template, url_for, flash
from main.models import Booking_date, Booking_time
from main import db, app
from datetime import datetime, timedelta
from main.booking.forms import Book_time

book = Blueprint('book', __name__)

@book.route('/', methods=['GET', 'POST'])
def index():

    form = Book_time()

    if form.validate_on_submit():
        if str(form.date_select.data) < datetime.now().strftime('%Y-%m-%d') or str(form.date_select.data) > (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d'):
            flash('The day you select is out of range! Choose the dates within one week from the present day.', category = 'warning')
            return redirect(url_for('book.index'))
        date = form.date_select.data
        if Booking_date.query.filter_by(book_on=date).first() != None:
            booking_full = Booking_date.query.filter_by(book_on=date).all()
            for booking in booking_full:
                if int(form.time_from.data) >= Booking_time.query.filter_by(book_on_id=booking.id).first().book_from and int(form.time_from.data) < Booking_time.query.filter_by(book_on_id=booking.id).first().book_to:
                    flash('The selected time is occupied already by another user!', category= 'warning')
                    return redirect(url_for('book.index'))
                if int(form.time_to.data) > Booking_time.query.filter_by(book_on_id=booking.id).first().book_from and int(form.time_to.data) <= Booking_time.query.filter_by(book_on_id=booking.id).first().book_to:
                    flash('The selected time is occupied already by another user!', category= 'warning')
                    return redirect(url_for('book.index'))

        bookday = Booking_date(book_on=form.date_select.data, book_by=form.name.data)
        db.session.add(bookday)
        db.session.commit()
        bookday_id = Booking_date.query.filter_by(book_on=form.date_select.data).order_by(Booking_date.id.desc()).first().id
        booktime = Booking_time(book_on_id=bookday_id, book_from=form.time_from.data, book_to=form.time_to.data)
        db.session.add(booktime)
        db.session.commit()

        flash('Booked successfully!', category='success')
        return redirect(url_for('book.index'))

    #today = datetime.now().strftime('%Y-%m-%d')
    database = Booking_date.query.filter(Booking_date.book_on >= datetime.now().strftime('%Y-%m-%d'), Booking_date.book_on <= (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d')).all()

    days = []
    for i in range(0,7):
        days.append((datetime.now() + timedelta(days=1)*i).strftime('%Y-%m-%d'))

    return render_template('index.html', form=form, database=database, days=days)
