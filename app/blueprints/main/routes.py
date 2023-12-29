from . import main
from flask_login import login_required, current_user
import requests
from flask import render_template, request, redirect, url_for, flash,jsonify
from app.models import BibleContents, User, db
from app.forms import Bible
from flask_cors import cross_origin


@main.route('/search', methods=["GET", 'POST'])
@cross_origin(headers=['Content-Type'])
def bibleSearch():
    form = Bible()

    if request.method == 'POST':
        search = form.bible_search.data

        url = f'https://bible-api.com/{str(search)}'
        response = requests.get(url)
        data = response.json()

        try:
            text = data['verses'][0]['text']
            verse = data['verses'][0]['verse']
            chapter = data['verses'][0]['chapter']
            book = data['verses'][0]['book_name']


            # db.session.add(new_verse)
            # db.session.commit()
            return jsonify( verse=verse,
                        text=text,
                        chapter=chapter,
                        book=book,)
        except IndexError:
            return redirect('/bug')

    else:
        return render_template('/bible_search.html', form=form)