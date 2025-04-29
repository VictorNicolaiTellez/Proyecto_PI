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
from db.favouritesDAO import * # get_fav_songs,get_fav_albums,get_fav_artists,add_song_fav,add_album_fav,add_artist_fav,get_all_favourites
from db.cartDAO import get_cart_items,  get_cart_cds, get_cart_merch, get_cart_songs, get_cart_vinyls, add_vinyl_to_cart, add_cd_to_cart, add_merch_to_cart, add_song_to_cart, delete_cart_vinyl, delete_cart_cd, delete_cart_merch, delete_cart_song, get_cart_quantity, update_cart_quantity
from decimal import Decimal;

import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from werkzeug.utils import secure_filename
from functools import wraps
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import random


app = Flask(__name__)

# Clave secreta para cifrar las cookies de sesión
app.secret_key = 'Key'
app.permanent_session_lifetime = timedelta(days=7)

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

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
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id'] 
    
    if exist_song_fav(user_id, song_id) == False:
        add_song_fav(user_id,song_id)
        flash('Cancion añadida a favoritos.')
    else:
        delete_fav_song(user_id, song_id)
        flash('Cancion eliminada de favoritos.')
    return redirect(request.referrer or url_for('index'))

@app.route('/add_album_fav/<int:album_id>', methods=['POST'])
@login_required
def album_fav(album_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']

    if exist_album_fav(user_id, album_id) == False:
        add_album_fav(user_id,album_id)
        flash('Álbum añadido a favoritos.')
    else:
        delete_fav_album(user_id, album_id)
        flash('Álbum eliminado de favoritos.')
    return redirect(request.referrer or url_for('index'))

@app.route('/add_artist_fav/<int:artist_id>', methods=['POST'])
@login_required
def artist_fav(artist_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id'] 
    
    if exist_artist_fav(user_id, artist_id) == False:
        add_artist_fav(user_id,artist_id)
        flash('Artista añadido a favoritos.')
    else:
        delete_fav_artist(user_id,artist_id)
        flash('Artista eliminado de favoritos.')
    return redirect(request.referrer or url_for('index'))


@app.route('/studio/')
@login_required
def studio():
    user_session = session.get('user')
    
    user= get_user_by_username(user_session['username'])
    user_id = user['id']  
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
        
        print("Contraseña escrita por el usuario:", passwd)
        print("Contraseña hash guardada:", user['password_hash'])
        print("Contraseña hash generada:", generate_password_hash(passwd))
        print("Comparación:", check_password_hash(user['password_hash'],passwd ))

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
    password_hash = generate_password_hash(new_user['passwd'], method='pbkdf2:sha256', salt_length=16)

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


@app.route('/firebase_login/', methods=['POST'])
def firebase_login():
    id_token = request.json.get('token')
    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        email = decoded_token['email']
        name = decoded_token.get('name', '')
        
        # Buscar en tu base de datos local
        user = get_user_by_email(email)
        if not user:
            # Registrar nuevo usuario en tu BD local
            user_data = {
                'username': email.split('@')[0],
                'fullname': name,
                'email': email,
                'passwd': '',  # No necesitas password
                'user_type': 'customer',
                'birthdate': '2020-01-01',  
            }
            add_user(user_data)
            user = get_user_by_email(email)

        # Crear la sesión Flask
        session['user'] = {
            'id': user['id'],
            'username': user['username'],
            'fullname': user['fullname'],
            'email': user['email'],
            'user_type': user['user_type'],
            'birthdate': user['birthdate']
        }
        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print(f"[ERROR] Firebase login: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 401

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile/')
@login_required
def profile():
    user = session.get('user')
    return render_template('user_profile.html', user=user)

@app.route('/edit_profile/', methods=['GET', 'POST'])
@login_required
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
@login_required
def carrito():
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id'] 
    
    # Obtener productos del carrito
    vinyls = [get_vinyl_by_id(vinyl_id[0]) for vinyl_id in get_cart_vinyls(user_id)]
    cds = [get_cd_by_id(cd_id[0]) for cd_id in get_cart_cds(user_id)]
    merch = [get_merch_by_id(merch_id[0]) for merch_id in get_cart_merch(user_id)]
    songs = [get_song_by_id(song_id[0]) for song_id in get_cart_songs(user_id)]
    
    # Calcular totales
    total_vinyls = sum(v['price']*v['quantity'] for v in vinyls)
    total_cds = sum(c['price']*c['quantity'] for c in cds)
    total_merch = sum(m['price']*m['quantity'] for m in merch)
    total_songs = sum(s['price'] for s in songs)
    
    subtotal = total_vinyls + total_cds + total_merch + total_songs
    shipping = Decimal('5.99') if subtotal > 0 else Decimal(0)  # Coste de envío fijo
    total = subtotal + shipping
    
    return render_template('carrito.html', 
                         vinyls=vinyls,
                         cds=cds,
                         merch=merch,
                         songs=songs,
                         subtotal=subtotal,
                         shipping=shipping,
                         total=total)

@app.route('/add_vinyl_cart/<int:vinyl_id>', methods=['POST'])
@login_required
def vinyl_cart(vinyl_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    add_vinyl_to_cart(user_id, vinyl_id)
    flash('Vinilo añadido al carrito.')
    return redirect(request.referrer or url_for('carrito'))

@app.route('/add_cd_cart/<int:cd_id>', methods=['POST'])
@login_required
def cd_cart(cd_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    add_cd_to_cart(user_id, cd_id)
    flash('CD añadido al carrito.')
    return redirect(request.referrer or url_for('carrito'))

@app.route('/add_merch_cart/<int:merch_id>', methods=['POST'])
@login_required
def merch_cart(merch_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    add_merch_to_cart(user_id, merch_id)
    flash('Producto de merchandising añadido al carrito.')
    return redirect(request.referrer or url_for('carrito'))

@app.route('/add_song_cart/<int:song_id>', methods=['POST'])
@login_required
def song_cart(song_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    add_song_to_cart(user_id, song_id)
    flash('Producto de merchandising añadido al carrito.')
    return redirect(request.referrer or url_for('carrito'))

@app.route('/remove_vinyl_cart/<int:vinyl_id>', methods=['POST'])
@login_required
def remove_vinyl_cart(vinyl_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    delete_cart_vinyl(vinyl_id)
    flash('Vinilo eliminado del carrito.')
    return redirect(url_for('carrito'))

@app.route('/remove_cd_cart/<int:cd_id>', methods=['POST'])
@login_required
def remove_cd_cart(cd_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    delete_cart_cd(cd_id)
    flash('Vinilo eliminado del carrito.')
    return redirect(url_for('carrito'))

@app.route('/remove_merch_cart/<int:merch_id>', methods=['POST'])
@login_required
def remove_merch_cart(merch_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    delete_cart_merch(merch_id)
    flash('Vinilo eliminado del carrito.')
    return redirect(url_for('carrito'))

@app.route('/remove_song_cart/<int:song_id>', methods=['POST'])
@login_required
def remove_song_cart(song_id):
    user_session = session.get('user')
    user= get_user_by_username(user_session['username'])
    user_id = user['id']
    delete_cart_song(song_id)
    flash('Vinilo eliminado del carrito.')
    return redirect(url_for('carrito'))

@app.route('/actualizar_cantidad', methods=['POST'])
@login_required
def actualizar_cantidad():
    user_session = session.get('user')
    user = get_user_by_username(user_session['username'])
    user_id = user['id']

    product_id = request.form.get('product_id')
    product_type = request.form.get('product_type')
    action = request.form.get('action')  # "incrementar" o "decrementar"
    current_quantity = int(request.form.get('quantity'))

    # Calcular nueva cantidad
    new_quantity = current_quantity
    if action == "incrementar":
        new_quantity += 1
    elif action == "decrementar" and current_quantity > 1:
        new_quantity -= 1

    # Actualizar la base de datos
    update_cart_quantity(new_quantity, user_id, product_id, product_type)

    return redirect(url_for('carrito'))