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

@app.route('/library/')
def library():
    return render_template('library.html')

@app.route('/store/')
def store():
    return render_template('store.html')

if __name__ == '__main__':
    app.run(debug=True)