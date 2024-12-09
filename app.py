# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('ice_cream.db')

@app.route('/add_flavor', methods=['POST'])
def add_flavor():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (name, description, availability) VALUES (?, ?, ?)', 
                   (data['name'], data['description'], data['availability']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Flavor added successfully!"})
@app.route('/')
def home():
    return "Welcome to the Ice Cream Parlor App!"
@app.route('/flavors', methods=['GET'])
def get_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    rows = cursor.fetchall()
    conn.close()

    flavors = [{"id": row[0], "name": row[1], "description": row[2], "availability": row[3]} for row in rows]
    return jsonify(flavors)
@app.route('/add_allergen', methods=['POST'])
def add_allergen():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customer_suggestions (suggestion, allergen) VALUES (?, ?)', 
                   (data['suggestion'], data['allergen']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Allergen added successfully!"})
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer_suggestions')
    rows = cursor.fetchall()
    conn.close()

    suggestions = [{"id": row[0], "suggestion": row[1], "allergen": row[2]} for row in rows]
    return jsonify(suggestions)


# Add other routes similarly (search, filter, add allergens, etc.)
if __name__ == "__main__":
    app.run(debug=True)

