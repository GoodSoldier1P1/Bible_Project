import requests

def bibleSearch(verse):
    url = f'https://bible-api.com/{verse}'
    response = requests.get(url)
    data = response.json()

    try:
        bible_dict = {
                    'book': data['verses'][0]['book_name'],
                    'chapter': data['verses'][0]['chapter'],
                    'verse': data['verses'][0]['verse'],
                    'text': data['verses'][0]['text']
                }
        return bible_dict
    except IndexError:
        return 'Please enter a valid verse.'
    
print(bibleSearch('2timothy 2:3'))