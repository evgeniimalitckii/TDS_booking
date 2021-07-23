from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, NumberRange
from wtforms import ValidationError

class Book_time(FlaskForm):
    date_select = DateField('Select date', format = '%Y-%m-%d', validators=[DataRequired()])
    #time_from = IntegerField('Time from', validators=[NumberRange(min=0, max=24)])
    time_from = SelectField('Time from:',
                        choices=[(1, '1 : 00'),
                                  (2, '2 : 00'),
                                  (3, '3 : 00'),
                                  (4, '4 : 00'),
                                  (5, '5 : 00'),
                                  (6, '6 : 00'),
                                  (7, '7 : 00'),
                                  (8, '8 : 00'),
                                  (9, '9 : 00'),
                                  (10, '10 : 00'),
                                  (11, '11 : 00'),
                                  (12, '12 : 00'),
                                  (13, '13 : 00'),
                                  (14, '14 : 00'),
                                  (15, '15 : 00'),
                                  (16, '16 : 00'),
                                  (17, '17 : 00'),
                                  (18, '18 : 00'),
                                  (19, '19 : 00'),
                                  (20, '20 : 00'),
                                  (21, '21 : 00'),
                                  (22, '22 : 00'),
                                  (23, '23 : 00'),
                                  (24, '24 : 00'),
                                  ], )
    #time_to = IntegerField('Time from', validators = [NumberRange(min=0, max=24)])
    time_to = SelectField('Time to (including):',
                        choices=[(1, '1 : 00'),
                                  (2, '2 : 00'),
                                  (3, '3 : 00'),
                                  (4, '4 : 00'),
                                  (5, '5 : 00'),
                                  (6, '6 : 00'),
                                  (7, '7 : 00'),
                                  (8, '8 : 00'),
                                  (9, '9 : 00'),
                                  (10, '10 : 00'),
                                  (11, '11 : 00'),
                                  (12, '12 : 00'),
                                  (13, '13 : 00'),
                                  (14, '14 : 00'),
                                  (15, '15 : 00'),
                                  (16, '16 : 00'),
                                  (17, '17 : 00'),
                                  (18, '18 : 00'),
                                  (19, '19 : 00'),
                                  (20, '20 : 00'),
                                  (21, '21 : 00'),
                                  (22, '22 : 00'),
                                  (23, '23 : 00'),
                                  (24, '24 : 00'),
                                  ], )
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Book')

    def validate_time(sef, time_from, time_to):
        if time_to < time_from:
            raise ValidationError(message='Selected time interval is invalid!')
