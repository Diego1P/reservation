from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class ReservationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10,max=11)])
    guests = SelectField('guests', coerce=int, choices = [(x, x) for x in range(1, 9)])

    submit = SubmitField('Reverse')