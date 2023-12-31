from app.blueprints.auth import auth
from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, request, redirect, url_for, flash, jsonify
from .forms import LoginForm, SignupForm
from app.models import User, BibleContents, db
from werkzeug.security import check_password_hash
import requests
from flask_cors import cross_origin


@auth.route('/', methods=['GET', 'POST'])
@cross_origin(headers=['Content-Type'])
def home():
    RandomVerseUrl = 'https://bible-api.com/?random=verse'
    RandomVerseResponse = requests.get(RandomVerseUrl)
    RandomVerseData = RandomVerseResponse.json()

    randomVerseText = RandomVerseData['verses'][0]['text']
    randomVerse = RandomVerseData['verses'][0]['verse']
    RandomChapter = RandomVerseData['verses'][0]['chapter']
    RandomBook = RandomVerseData['verses'][0]['book_name']
    reference = RandomVerseData['reference']

    return jsonify( randomVerse=randomVerse,
                    randomVerseText=randomVerseText,
                    RandomChapter=RandomChapter,
                    RandomBook=RandomBook,
                    reference=reference,)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit:
        email = form.email.data
        password = form.password.data

        queried_user = User.query.filter(User.email == email).first()
        print(queried_user)
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f"Hello, {queried_user.first_name}!", 'success')
            return redirect(url_for('main.bibleSearch'))
        else:
            flash("Invalid Email or Password", 'danger')
            return ("Invalid Email or Password")
    else:
        return render_template('login.html', form=form)
    

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        user = User(first_name, last_name, email, password)

        db.session.add(user)
        db.session.commit()

        flash(f"Thank you {first_name}, for siging up!", 'success')
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)