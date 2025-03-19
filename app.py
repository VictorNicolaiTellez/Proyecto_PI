import os
from flask import Flask, render_template
from flask import redirect, url_for
from flask import request, session,jsonify
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)





"""
Carga de datos de los archivos JSON al iniciar la API
"""
with open('static/json/songs.json') as json_file:
    data_json = json_file.read()
songs_list = json.loads(data_json)
with open('static/json/artists.json') as json_file:
    data_json = json_file.read()
artists_list = json.loads(data_json)
with open('static/json/albums.json') as json_file:
    data_json = json_file.read()
albums_list = json.loads(data_json)
with open('static/json/vinyls.json') as json_file:
    data_json = json_file.read()
vinyls_list = json.loads(data_json)
with open('static/json/cds.json') as json_file:
    data_json = json_file.read()
cds_list = json.loads(data_json)
with open('static/json/merchandising.json') as json_file:
    data_json = json_file.read()
merchandising_list = json.loads(data_json)
with open('static/json/users.json') as json_file:
    data_json = json_file.read()
users_list = json.loads(data_json)
with open('static/json/users_artists.json') as json_file:
    data_json = json_file.read()
users_artists_list = json.loads(data_json)

print(users_list)
users_list.append({ 'username':'admin', 'fullname':'admin istrador', 'email':'admin@admin.com', 'birthdate':'01-01-0001', 'passwd':'admin1234' })
print("editado")
print(users_list)


@app.route('/')
def index():
    return render_template('index.html',songs=songs_list)

@app.route('/songs/')
def songs():
    return render_template('songs.html')

@app.route('/explorer/', methods=["GET"])
def explorer():
    music_search = request.args.get('music_search','')
    if music_search == '':
        return render_template('explorer.html', songs=songs_list, artists=artists_list, albums=albums_list)
    search = music_search.lower()
    songs_filter = [item for item in songs_list if search in item["name"].lower()]
    artists_filter = [item for item in artists_list if search in item["name"].lower()]
    albums_filter = [item for item in albums_list if search in item["name"].lower()]
    return render_template('explorer.html', songs=songs_filter, artists=artists_filter, albums=albums_filter)

@app.route('/store/', methods=["GET"])
def store():
    store_search = request.args.get('store_search','')
    if store_search == '':
        return render_template('store.html', vinyls=vinyls_list, cds=cds_list, merchandising=merchandising_list)
    search = store_search.lower()
    vinyls_filter = [item for item in vinyls_list if search in item["name"].lower()]
    cds_filter = [item for item in cds_list if search in item["name"].lower()]
    merchandising_filter = [item for item in merchandising_list if search in item["name"].lower()]
    return render_template('store.html', vinyls=vinyls_filter, cds=cds_filter, merchandising=merchandising_filter)

@app.route('/library/', methods=['GET'])
def library():
    library_search = request.args.get('library_search','')

    return render_template('library.html')

@app.route('/studio/')
def studio():
    return render_template('studio.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    new_user = request.form
    dict = {'username':new_user.get('username'), 'fullname':new_user.get('fullname')}
    if new_user.get('nombre-artistico'):
        dict.update({'artistname':new_user.get('artistname')})
        users_artists_list.append(new_user.to_dict())
        print("------LISTA ARTISTAS USUARIOS------")
        print(users_artists_list)
        return render_template('signup.html')
    users_list.append(new_user.to_dict())
    print("------LISTA USUARIOS------")
    print(users_list)
    return render_template('signup.html')

@app.route('/studio/song_upload')
def song_upload():
    return render_template('song_upload.html')

@app.route('/profile/')
def profile():
    
    return render_template('user_profile.html')




if __name__ == '__main__':
    app.run(debug=True)