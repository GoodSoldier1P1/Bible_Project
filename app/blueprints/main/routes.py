from . import main
from flask_login import login_required, current_user
import requests
from flask import render_template, request, redirect, url_for, flash
from app.models import BibleContents, User, db
from app.forms import Bible

@main.route('/search', methods=["GET", 'POST'])
#add login required if api works and is what we are going for. AFTER creating signup and login
def bibleSearch():
    form = Bible()

    if request.method == 'POST':
        search = form.bible_search.data
        verse = BibleContents.query.filter_by(BibleContents.book_id.ilike(search)).first()

        if verse:
            print("Searching for the verse")

            all_verses = {
                'book': verse.book_id,
                'chapter': verse.chapter,
                'verse': verse.verse,
                'text': verse.text
            }

            return render_template('/bible_search.html', form=form, all_verses=all_verses)
        
        else:
            print("Did Not Find verse in database, calling API")
            url = f'https://bible-api.com/{str(search)}'
            response = requests.get(url)
            data = response.json

            try:
                bible_dict = {
                    'book': data['verses'][0]['book_name'],
                    'chapter': data['verses'][0]['chapter'],
                    'verse': data['verses'][0]['verse'],
                    'text': data['verses'][0]['text']
                }

                print(bible_dict)

                new_verse = BibleContents(book_id=bible_dict['book'],
                                          chapter=bible_dict['chapter'],
                                          verse=bible_dict['verse'],
                                          text=bible_dict['text'])

                db.session.add(new_verse)
                db.session.commit()

                return render_template('/bible_search.html', form=form, all_verses=all_verses)
            except IndexError:
                return redirect('/bug')

    else:
        return render_template('/bible_search.html', form=form)