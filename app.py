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

@app.route('/store/')
def store():
    return render_template('store.html')

@app.route('/store/', methods=['GET'])
def search():
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