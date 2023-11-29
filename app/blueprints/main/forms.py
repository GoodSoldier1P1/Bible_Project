from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BibleSearch(FlaskForm):
    verse = StringField('What verse would you like to read? \nYou can search for one verse or multiple (2 Timothy 2:3-7)', validators=[DataRequired()])
    submit_btn = SubmitField('Search')