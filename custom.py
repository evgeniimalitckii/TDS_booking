from main.models import Booking_date, Booking_time
from main import db
from datetime import datetime, timedelta

data = '2021-07-23'

#print(data)
#print(Booking_date.query.first().id)
#print(Booking_date.query.filter_by(book_on=data).first().id)
#print(Booking_date.query.filter_by(book_on=data).order_by(Booking_date.id.desc()).first().id)

#book_id = Booking_date.query.first().id

#print(Booking_time.query.filter_by(book_on_id=book_id).first().book_to)

#print(Booking_time.query.order_by(Booking_time.id.desc()).first().book_from)
#print(Booking_time.query.order_by(Booking_time.id.desc()).first().book_to)
#rint(Booking_date.query.order_by(Booking_date.id.desc()).first().time[0].book_from)
#print(Booking_date.query.order_by(Booking_date.id.desc()).first().time[0].book_to)

#database = Booking_date.query.filter(Booking_date.book_on >= datetime.now().strftime('%Y-%m-%d'), Booking_date.book_on <= (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d')).all()
#print (database)
#print(database[1].time[0].book_from)

#days = []
#for i in range(0,7):
#    days.append((datetime.now() + timedelta(days=1)*i).strftime('%Y-%m-%d'))
#print(days)

#database = Booking_date.query.filter(Booking_date.book_on >= datetime.now().strftime('%Y-%m-%d'), Booking_date.book_on <= (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d')).all()
#for date in database:
#    print(date.book_on)

#print(str(days[0]), str(database[0].book_on))

##if (days[0]) == str(database[0].book_on):
#    print("TRUE")
#else:
#    print("FALSE")

print((datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d'))
