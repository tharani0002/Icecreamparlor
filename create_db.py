# create_db.py
import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            availability TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY,
            ingredient_name TEXT,
            stock INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY,
            suggestion TEXT,
            allergen TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created!")
