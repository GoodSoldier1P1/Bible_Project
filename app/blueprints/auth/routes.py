from app.blueprints.auth import auth
from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, request, redirect, url_for, flash
from .forms import LoginForm, SignupForm
from app.models import User, BibleContents, db
from werkzeug.security import check_password_hash

@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit:
        email = form.email.data
        password = form.password.data

        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f"Hello, {queried_user.first_name}!", 'success')
            return render_template('main.bible_search.html')
        else:
            return "Invalid Email or Password"
    else:
        return render_template('login.html', form=form)