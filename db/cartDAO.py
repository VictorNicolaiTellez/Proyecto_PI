# db/cartDAO.py
from .dbconnection import connection

def get_cart_items(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cart")
    cart = cursor.fetchall()
    cursor.close()
    return cart

def get_cart_vinyls(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id = %s AND product_type = 'vinyl'", (user_id,))
    cart = cursor.fetchall()
    cursor.close()
    return cart 

def get_cart_cds(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id = %s AND product_type = 'cd'", (user_id,))
    cart = cursor.fetchall()
    cursor.close()
    return cart

def get_cart_merch(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id = %s AND product_type = 'merch'", (user_id,))
    cart = cursor.fetchall()
    cursor.close()
    return cart

def get_cart_songs(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id = %s AND product_type = 'song'", (user_id,))
    cart = cursor.fetchall()
    cursor.close()
    return cart

def add_vinyl_to_cart(user_id, vinyl_id):
    
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO cart (user_id, product_id, product_type, quantity)
            VALUES (%s, %s, 'vinyl', 1)
            ON DUPLICATE KEY UPDATE 
            quantity = quantity + VALUES(quantity);
        """, (user_id, vinyl_id))
    connection.commit()
    cursor.close()

def add_cd_to_cart(user_id, cd_id):
    
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO cart (user_id, product_id, product_type, quantity)
            VALUES (%s, %s, 'cd', 1)
            ON DUPLICATE KEY UPDATE 
            quantity = quantity + VALUES(quantity);
        """, (user_id, cd_id))
    connection.commit()
    cursor.close()

def add_merch_to_cart(user_id, merch_id):
    
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO cart (user_id, product_id, product_type, quantity)
            VALUES (%s, %s, 'merch', 1)
            ON DUPLICATE KEY UPDATE 
            quantity = quantity + VALUES(quantity);
        """, (user_id, merch_id))
    connection.commit()
    cursor.close()

def add_song_to_cart(user_id, song_id):
    
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO cart (user_id, product_id, product_type, quantity)
            VALUES (%s, %s, 'song', 1)
            ON DUPLICATE KEY UPDATE 
            quantity = quantity + VALUES(quantity);
        """, (user_id, song_id))
    connection.commit()
    cursor.close()

def delete_cart_vinyl(vinyl_id):
    
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cart WHERE product_id = %s", (vinyl_id,))
    connection.commit()
    cursor.close()

def delete_cart_cd(cd_id):
    
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cart WHERE product_id = %s", (cd_id,))
    connection.commit()
    cursor.close()

def delete_cart_merch(merch_id):
    
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cart WHERE product_id = %s", (merch_id,))
    connection.commit()
    cursor.close()

def delete_cart_song(song_id):
    
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cart WHERE product_id = %s", (song_id,))
    connection.commit()
    cursor.close()

def get_cart_quantity(user_id, product_id, product_type):
    
    cursor = connection.cursor()
    cursor.execute("""
        SELECT quantity FROM cart 
        WHERE user_id = %s AND product_id = %s AND product_type = %s
    """, (user_id, product_id, product_type))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 0

def update_cart_quantity(new_quantity, user_id, product_id, product_type):
    
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE cart 
        SET quantity = %s 
        WHERE user_id = %s 
        AND product_id = %s 
        AND product_type = %s
    """, (new_quantity, user_id, product_id, product_type))
    connection.commit()
    cursor.close()