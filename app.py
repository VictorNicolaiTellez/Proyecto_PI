from urllib.parse import unquote
import os
from flask import Flask, render_template
from flask import redirect, url_for
from flask import request, session,jsonify
import json
from werkzeug.utils import secure_filename
from flask import send_from_directory

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

@app.route('/')
def index():
    return render_template('index.html',songs=songs_list)

@app.route("/songs/<id>")
#def detalle_cancion(id):
def songs_details(id):
    song = [item for item in songs_list if item["id"] == int(id)]
    
    if song:
        audio_filename = "night-detective-226857.mp3"  # El nombre del archivo de audio
        return render_template("songs.html", song=song[0],audio_filename=audio_filename)
    return "Cancion no encontrada"-404 

@app.route("/artists/<id>")
def artists_details(id):
    artist = [item for item in artists_list if item["id"] == int(id)]
    
    if artist:
        audio_filename = "night-detective-226857.mp3"  # El nombre del archivo de audio
        return render_template("info_artist.html", artist=artist[0])
    return "Artista no encontrado"-404 

@app.route("/albums/<id>")
def albums_details(id):
    album = [item for item in albums_list if item["id"] == int(id)]
    
    if album:
        audio_filename = "night-detective-226857.mp3"  # El nombre del archivo de audio
        return render_template("info_album.html", album=album[0])
    return "Álbum no encontrado"-404 

@app.route("/vinyls/<id>")
def vinyls_details(id):
    vinyl = [item for item in vinyls_list if item["id"] == int(id)]
    if vinyl:
        return render_template("info_vinil.html", vinyl=vinyl[0])
    return "Vinilo no encontrado"-404 


@app.route("/cds/<id>")
def cds_details(id):
    cd = [item for item in cds_list if item["id"] == int(id)]

    if cd:
        return render_template("info_cd.html", cd=cd[0])
    return "CD no encontrado"-404 

@app.route("/merchandising/<id>")
def merch_details(id):    
    merch = [item for item in merchandising_list if item["id"] == int(id)]

    if merch:
        return render_template("info_merch.html", merch=merch[0])
    return "Merchandising no encontrado"-404 


@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory('audio', filename) 


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
    return render_template('studio.html',songs = songs_list)

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')

        # Simulación de autenticación (cámbialo con tu lógica real)
        # if usuario == "admin" and contraseña == "1234":
        return redirect(url_for('profile'))  # Redirige al perfil

       # return "Credenciales incorrectas", 401  # Mensaje de error si falla

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

@app.route('/edit_profile/' ,methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
    
        return redirect(url_for('profile'))  # Redirige al perfil
    
    return render_template('edit_profile.html')




if __name__ == '__main__':
    app.run(debug=True)