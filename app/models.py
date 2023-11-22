from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class BibleContents(db.Model):
    book_id = db.Column(db.String, primary_key=True)
    chapter = db.Column(db.Integer)
    verse = db.Column(db.Integer)
    text = db.Column(db.String)

    def __init__(self, book_id, chapter, verse, text):
        self.book_id = book_id
        self.chapter = chapter
        self.verse = verse
        self.text = text