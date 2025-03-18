from flask import Flask, render_template
from flask import redirect, url_for
from flask import request, session,jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/songs/')
def songs():
    return render_template('songs.html')

@app.route('/explorer/')
def explorer():
    songs = [
    {"id":"0","album":"Tribute","artist":"John Newman","duration":"4:00","genre":"0","name":"Love Me Again","rank_time":"2"},
    {"id":"1","album":"V","artist":"Maroon 5","duration":"3:10","genre":"0","name":"Maps","rank_time":"1"},
    {"id":"2","album":"A Head Full of Dreams","artist":"Coldplay","duration":"4:24","genre":"0","name":"Adventure of a Lifetime","rank_time":"1"},
    {"id":"3","album":"Boulevard of Broken Dreams","artist":"Green Day","duration":"4:21","genre":"0","name":"Boulevard of Broken Dreams","rank_time":"2"},
    {"id":"4","album":"V","artist":"Maroon 5","duration":"3:51","genre":"0","name":"Animals","rank_time":"1"},
    {"id":"5","album":"Overexposed Track By Track","artist":"Maroon 5","duration":"3:40","genre":"0","name":"One More Night","rank_time":"0"},
    {"id":"6","album":"(What's The Story) Morning Glory?","artist":"Oasis","duration":"4:19","genre":"0","name":"Wonderwall","rank_time":"0"},
    {"id":"7","album":"Favourite Worst Nightmare","artist":"Arctic Monkeys","duration":"4:14","genre":"0","name":"505","rank_time":"0"},
    {"id":"8","album":"Overexposed Track By Track","artist":"Maroon 5, Wiz Khalifa","duration":"3:51","genre":"0","name":"Payphone","rank_time":"1"},
    {"id":"9","album":"A Head Full of Dreams","artist":"Coldplay","duration":"4:18","genre":"0","name":"Hymn for the Weekend","rank_time":"2"}
]
    return render_template('explorer.html', songs=songs)

@app.route('/explorer/', methods=['GET'])
def search_explorer():
    return render_template('explorer.html')

@app.route('/store/')
def store():
    return render_template('store.html')

@app.route('/store/', methods=['GET'])
def search_store():
    data = request.form
    content = data.get('query', type=str)
    
    return render_template('store.html', content=content)

@app.route('/library/')
def library():
    return render_template('library.html')

@app.route('/studio/')
def studio():
    return render_template('studio.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/studio/song_upload')
def song_upload():
    return render_template('song_upload.html')


if __name__ == '__main__':
    app.run(debug=True)