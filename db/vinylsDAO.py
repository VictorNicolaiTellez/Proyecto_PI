# db/vinylsDAO.py
from .dbconnection import connection

def get_all_vinyls():
    """Obtiene todos los vinilos"""
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vinyls")
    vinyls = cursor.fetchall()
    cursor.close()
    return vinyls

def get_vinyl_by_id(vinyl_id):
    """Obtiene un vinilo por su ID"""
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vinyls WHERE id = %s", (vinyl_id,))
    vinyl = cursor.fetchone()
    cursor.close()
    return vinyl

def add_vinyl(vinyl_data):
    """Agrega un nuevo vinilo a la base de datos"""
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO vinyls (name, artist_id, release_date, genre, price) VALUES (%s, %s, %s, %s, %s)",
                   (vinyl_data['name'], vinyl_data['artist_id'], vinyl_data['release_date'], vinyl_data['genre'], vinyl_data['price']))
    connection.commit()
    cursor.close()

def update_vinyl(vinyl_id, vinyl_data):
    """Actualiza los datos de un vinilo en la base de datos"""
    
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE vinyls
        SET name = %s, artist_id = %s, release_date = %s, genre = %s, price = %s
        WHERE id = %s
    """, (vinyl_data['name'], vinyl_data['artist_id'], vinyl_data['release_date'], vinyl_data['genre'], vinyl_data['price'], vinyl_id))
    connection.commit()
    cursor.close()

def delete_vinyl(vinyl_id):
    """Elimina un vinilo de la base de datos"""
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM vinyls WHERE id = %s", (vinyl_id,))
    connection.commit()
    cursor.close()



def get_vinyls_by_name(name):

    cursor = connection.cursor()
    query = "SELECT * FROM vinyls WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    cursor.close()
    return result
