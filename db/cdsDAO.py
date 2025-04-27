# db/cdsDAO.py
from .dbconnection import connection

def get_all_cds():
    """Obtiene todos los CDs"""
     
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cds")
    cds = cursor.fetchall()
    cursor.close()
    return cds

def get_cd_by_id(cd_id):
    """Obtiene un CD por su ID"""
     
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cds WHERE id = %s", (cd_id,))
    cd = cursor.fetchone()
    cursor.close()
    return cd

def add_cd(cd_data):
    """Agrega un nuevo CD a la base de datos"""
     
    cursor = connection.cursor()
    cursor.execute("INSERT INTO cds (name, artist_id, release_date, genre, price) VALUES (%s, %s, %s, %s, %s)",
                   (cd_data['name'], cd_data['artist_id'], cd_data['release_date'], cd_data['genre'], cd_data['price']))
    cursor.commit()
    cursor.close()

def update_cd(cd_id, cd_data):
    """Actualiza los datos de un CD en la base de datos"""
     
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE cds
        SET name = %s, artist_id = %s, release_date = %s, genre = %s, price = %s
        WHERE id = %s
    """, (cd_data['name'], cd_data['artist_id'], cd_data['release_date'], cd_data['genre'], cd_data['price'], cd_id))
    cursor.commit()
    cursor.close()

def delete_cd(cd_id):
    """Elimina un CD de la base de datos"""
     
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cds WHERE id = %s", (cd_id,))
    cursor.commit()
    cursor.close()

def get_cds_by_name(name):
    cursor = connection.cursor()
    query = "SELECT * FROM cds WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    cursor.close()
    return result