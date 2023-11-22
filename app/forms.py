from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class Bible(FlaskForm):
    bible_search = StringField('What verse or passage is on your mind?', validators=[DataRequired()])
    submit_btn = SubmitField('Search')