from datetime import datetime, timedelta
from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify
from flask import send_from_directory

from db.dbconnection import dbConnect
from db.songsDAO import add_song, get_all_songs, get_song_by_id,get_songs_by_album,get_songs_by_artist, get_songs_by_name, update_song
from db.albumsDAO import album_exists_for_artist, get_albums_by_name, get_all_albums, get_album_by_id, get_albums_by_artist, add_album, update_album, delete_album
from db.vinylsDAO import get_all_vinyls, get_vinyl_by_id, add_vinyl, get_vinyls_by_name, update_vinyl, delete_vinyl
from db.cdsDAO import get_all_cds, get_cd_by_id, add_cd, get_cds_by_name, update_cd, delete_cd
from db.merchandisingDAO import get_all_merch, get_merch_by_id,add_merch, get_merchandising_by_name, update_merch, delete_merch
from db.usersDAO import get_all_users, get_user_by_email, add_user, update_user, get_user_by_email_and_password,get_user_by_username,get_user_by_id,get_all_artists,get_artists_by_name
from db.favouritesDAO import get_fav_songs,get_fav_albums,get_fav_artists,add_song_fav,add_album_fav,add_artist_fav,get_all_favourites

from werkzeug.utils import secure_filename
from functools import wraps
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import random


app = Flask(__name__)

# Clave secreta para cifrar las cookies de sesión
app.secret_key = 'Key'
app.permanent_session_lifetime = timedelta(days=7)

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapped

@app.route('/')
def index():
    songs = get_all_songs()

    shuffled = random.sample(songs, k=len(songs))  # Barajamos la lista de canciones
    carrusel1 = shuffled[0:10]
    carrusel2 = shuffled[10:20]
    carrusel3 = shuffled[20:30]
   
    return render_template('index.html',  
    carrusel1=carrusel1,
    carrusel2=carrusel2,
    carrusel3=carrusel3)

@app.route("/songs/<int:id>")
def songs_details(id):
    song = get_song_by_id(id)
    if song:
        album = get_album_by_id(song['album_id'])
        audio_filename = "night-detective-226857.mp3"  # este es fijo por ahora
        return render_template("songs.html", song=song, album=album, audio_filename=audio_filename)
    return "Canción no encontrada", 404 

@app.route('/artists/<int:artist_id>')
def artist_details(artist_id):
    artist = get_user_by_id(artist_id)  # Este ID debe ser el de users.id
    songs = get_song_by_id(artist_id)
    albums = get_all_albums()
    return render_template("info_artist.html", artist=artist, songs=songs, albums=albums)


@app.route('/albums/<int:album_id>')
def album_details(album_id):
    print(f"album_id recibido: {album_id}")
    album = get_album_by_id(album_id)
    if album:
        songs = get_songs_by_album(album_id)
        artist = get_user_by_id(album[1])  # si quieres mostrar también el artista
        return render_template("info_album.html", album=album, songs=songs, artist=artist)
    return "Álbum no encontrado", 404

@app.route("/vinyls/<id>")
def vinyls_details(id):
    vinyl = get_vinyl_by_id(id)
    if vinyl:
        return render_template("info_vinil.html", vinyl=vinyl)
    return "Vinilo no encontrado", 404 

@app.route("/cds/<id>")
def cds_details(id):
    cd = get_cd_by_id(id)
    if cd:
        return render_template("info_cd.html", cd=cd)
    return "CD no encontrado", 404 

@app.route("/merchandising/<id>")
def merch_details(id):    
    merch = get_merch_by_id(id)
    if merch:
        return render_template("info_merch.html", merch=merch)
    return "Merchandising no encontrado", 404

@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory('audio', filename) 

@app.route('/explorer/', methods=["GET"])
def explorer():
    music_search = request.args.get('music_search','')
    if music_search == '':
        songs = get_all_songs()
        artists = get_all_artists()
        albums = get_all_albums() 
        return render_template('explorer.html', songs=songs, artists=artists, albums=albums)
    search = music_search.lower()
    songs_filter = get_songs_by_name(search)
    artists_filter = get_artists_by_name(search)
    albums_filter = get_albums_by_name(search)
    return render_template('explorer.html', songs=songs_filter, artists=artists_filter, albums=albums_filter)

@app.route('/store/', methods=["GET"])
def store():
    store_search = request.args.get('store_search','')
    if store_search == '':
        vinyls = get_all_vinyls()
        cds = get_all_cds()
        merchandising = get_all_merch()
        return render_template('store.html', vinyls=vinyls, cds=cds, merchandising=merchandising)
    search = store_search.lower()
    vinyls_filter = get_vinyls_by_name(search)
    cds_filter = get_cds_by_name(search)
    merchandising_filter = get_merchandising_by_name(search)
    return render_template('store.html', vinyls=vinyls_filter, cds=cds_filter, merchandising=merchandising_filter)

@app.route('/library/', methods=['GET'])
@login_required
def library():
    
    library_search = request.args.get('library_search','')
    user_session = session.get('user')
    
    user= get_user_by_username(user_session['username'])
    user_id = user['id']  
    
    fav_song_ids = get_fav_songs(user_id)
    fav_album_ids = get_fav_albums(user_id) 
    fav_artist_ids = get_fav_artists(user_id)
        
    if library_search == '':
    
        songs = [get_song_by_id(song_id[0]) for song_id in fav_song_ids]
        albums = [get_album_by_id(album_id[0]) for album_id in fav_album_ids]
        artists = [get_user_by_id(artist_id[0]) for artist_id in fav_artist_ids]

        return render_template('library.html', songs=songs, artists=artists, albums=albums)
    else:
        search = library_search.lower()
        songs_filter = get_songs_by_name(search)
        artists_filter = get_artists_by_name(search)
        albums_filter = get_albums_by_name(search)

        # Filtrar solo los que están en favoritos
        songs = [s for s in songs_filter if s['id'] in fav_song_ids]
        artists = [a for a in artists_filter if a['id'] in fav_artist_ids]
        albums = [a for a in albums_filter if a['id'] in fav_album_ids]
        return render_template('library.html', songs=songs_filter, artists=artists_filter, albums=albums_filter)

@app.route('/add_song_fav/<int:song_id>', methods=['POST'])
@login_required
def song_fav(song_id):
    user_id = session.get('user')
    add_song_fav(user_id,song_id)
    flash('Cancion añadido a favoritos.')
    return redirect(request.referrer or url_for('index'))

@app.route('/add_album_fav/<int:album_id>', methods=['POST'])
@login_required
def album_fav(album_id):
    user_id = session.get('user')
    add_album_fav(user_id,album_id)
    flash('Ártista añadido a favoritos.')
    return redirect(request.referrer or url_for('index'))

@app.route('/add_artist_fav/<int:artist_id>', methods=['POST'])
@login_required
def artist_fav(artist_id):
    user_id = session.get('user')
    add_artist_fav(user_id,artist_id)
    flash('Artista añadido a favoritos.')
    return redirect(request.referrer or url_for('index'))


@app.route('/studio/')
#@login_required
def studio():
    user_session = session.get('user')
    
    user= get_user_by_username(user_session['username'])
    user_id = 1 # user['id']  
    songs = get_songs_by_artist(user_id)
    
    return render_template('studio.html',songs=songs)

@app.route('/song_upload/', methods=['GET', 'POST'])
@login_required
def song_upload():
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    if request.method == 'POST':
        new_song = request.form.to_dict()
 
        
        album_title = new_song.get('album')

        # Paso 1-3: Obtener o crear el álbum y conseguir su ID
        album_id = album_exists_for_artist(album_title, user['id'])
        if album_id is None:
            # Si no existe, lo creamos
            album_data = {
                'title': album_title,
                'artist': user['id'],
                'genre': new_song.get('genre')
            }
            add_album(album_data)
            # Ahora obtenemos el ID del álbum recién creado 
            album_id = album_exists_for_artist(album_title, user['id'])
 
        song_data = {
            'title': new_song.get('song'),
            'duration': new_song.get('duration'),
            'audio_file': new_song.get('audio_file'),
            'price': new_song.get('price'),
            'album': album_id,  # Usamos el ID del álbum existente o recién creado
            'artist': user['id']
        }
        add_song(song_data)  # Usamos el DAO para agregar una nueva canción
        
        return redirect(url_for('studio'))

    return render_template('song_upload.html')

@app.route('/song_edit/<int:song_id>', methods=['GET', 'POST'])
@login_required
def song_edit(song_id):
    song = get_song_by_id(song_id)  # Obtener la canción desde la base de datos usando song_id
    artist= get_user_by_id(song['artist_id'])  # Obtener el artista de la canción
    if request.method == 'POST':
        updated_song = {
            'title': request.form.get('song-title'),
            'price': request.form.get('price')
        }
        # Lógica para actualizar la canción con los nuevos datos
        update_song(song_id, updated_song)  # Usamos el DAO para actualizar la canción
        
        return redirect(url_for('studio'))  # Redirigir después de guardar los cambios
    
    return render_template('edit_song.html', song=song,artist=artist)  


'''

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        print("[DEBUG] Usuario ya en sesión, redirigiendo al perfil")
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        passwd = request.form.get('passwd')
        
        print(f"[DEBUG] Login recibido - Email: {email}, Contraseña: {passwd}")

        user = get_user_by_email_and_password(email, passwd)

        if user:
            print(f"[DEBUG] Usuario encontrado: {user['username']}")
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)

            # Estructura de sesión según tipo de usuario
            user_session = {
                'id': user['id'],
                'username': user['username'],
                'fullname': user['fullname'],
                'email': user['email'],
                'user_type': user['user_type'],
                'birthdate': user['birthdate'].strftime('%Y-%m-%d') if user['birthdate'] else None,
                'profile_image': user.get('profile_image') or ''
                
            }

            if user['user_type'] == 'artist':
                user_session['biography'] = user.get('biography')
                user_session['record'] = user.get('record')
                user_session['genre'] = user.get('genre')

            session['user'] = user_session
            return redirect(url_for('profile'))

        print("[DEBUG] Usuario no encontrado o contraseña incorrecta")
        error = "Credenciales incorrectas"
        return render_template('login.html', error=error)

    print("[DEBUG] Petición GET al login")
    return render_template('login.html')

    '''

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        print("[DEBUG] Usuario ya en sesión, redirigiendo al perfil")
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        passwd = request.form.get('passwd')
        
        print(f"[DEBUG] Login recibido - Email: {email}, Contraseña: {passwd}")

        # Obtener el usuario por email
        user = get_user_by_email(email)

        if user:
            # Verificar si la contraseña coincide con el hash almacenado
            if check_password_hash(user['password_hash'], passwd):
                print(f"[DEBUG] Usuario encontrado: {user['username']}")
                session.permanent = True
                app.permanent_session_lifetime = timedelta(days=7)

                # Estructura de sesión según tipo de usuario
                user_session = {
                    'id': user['id'],
                    'username': user['username'],
                    'fullname': user['fullname'],
                    'email': user['email'],
                    'user_type': user['user_type'],
                    'birthdate': user['birthdate'].strftime('%Y-%m-%d') if user['birthdate'] else None,
                    'profile_image': user.get('profile_image') or ''
                }

                if user['user_type'] == 'artist':
                    user_session['biography'] = user.get('biography')
                    user_session['record'] = user.get('record')
                    user_session['genre'] = user.get('genre')

                session['user'] = user_session
                return redirect(url_for('profile'))

        print("[DEBUG] Usuario no encontrado o contraseña incorrecta")
        error = "Credenciales incorrectas"
        return render_template('login.html', error=error)

    print("[DEBUG] Petición GET al login")
    return render_template('login.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    new_user = request.form.to_dict()

    if get_user_by_email(new_user['email']):
        return render_template('signup.html', error="Este correo ya está registrado")
    if get_user_by_username(new_user['username']):
        return render_template('signup.html', error="Este nombre de usuario ya existe")

    if new_user['passwd'] != new_user['confirm-passwd']:
        return render_template('signup.html', error="Las contraseñas no coinciden")

    # Hash de la contraseña
    password_hash = generate_password_hash(new_user['passwd'])

    user_data = {
        'username': new_user['username'],
        'fullname': new_user['fullname'],
        'email': new_user['email'],
        'passwd': password_hash,
        'user_type': new_user.get('user_type', 'customer'),  # 'customer' por defecto si no se especifica
        'birthdate': new_user['birthdate'],
        'biography': new_user.get('biography', ''),
        'record': new_user.get('record', ''),
        'genre': new_user.get('genre', '')
    }

    add_user(user_data)  # Usamos el DAO para agregar un nuevo usuario

    session['user'] = {
        'id': user_data['id'],  # Asumiendo que el ID se genera al insertar en la base de datos
        'username': user_data['username'],
        'fullname': user_data['fullname'],
        'email': user_data['email'],
        'user_type': user_data['user_type'],
        'birthdate': user_data['birthdate'],
    }

    # Si el usuario es artista, añadir los campos extras a la sesión
    if user_data['user_type'] == 'artist':
        session['user'].update({
            'biography': user_data['biography'],
            'record': user_data['record'],
            'genre': user_data['genre'],
        })

    # Redirigir al perfil
    return redirect(url_for('profile'))


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile/')
@login_required
def profile():
    user = session.get('user')
    return render_template('user_profile.html', user=user)

@app.route('/edit_profile/', methods=['GET', 'POST'])
def edit_profile():
    print(session['user'])  # Para depurar y ver qué contiene la sesión


    if request.method == 'POST':
        # Obtener los datos del formulario
        updated_user = {
            'fullname': request.form['fullname'],
            'username': request.form['username'],
            'email': request.form['email'],
            'birthdate': request.form['birthdate'],
            'record': request.form.get('record'),
            'genre': request.form.get('genre')
        }

        # Si el usuario introdujo una nueva contraseña, la actualizamos
        new_password = request.form.get('passwd')
        if new_password:
            updated_user['password_hash'] = generate_password_hash(new_password)
        #else:
            # Si no hay nueva contraseña, usamos la que ya teníamos en sesión
            #updated_user['password_hash'] = session['user']['password_hash']

        # Mantenemos el tipo de usuario también
        updated_user['user_type'] = session['user']['user_type']

        # Actualizar la sesión
        session['user'].update(updated_user)

        # Actualizar en la base de datos
        update_user(session['user']['id'], session['user'])

        return redirect(url_for('profile'))

    return render_template('edit_profile.html', user=session['user'])

@app.route('/carrito/')
def carrito():
    return render_template('carrito.html')
