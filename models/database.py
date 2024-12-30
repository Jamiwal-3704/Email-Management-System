import sqlite3

def connect_db():
    conn = sqlite3.connect('email_management.db')
    return conn

def get_templates():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM templates")
    templates = cursor.fetchall()
    conn.close()
    return templates

def save_template(template):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO templates (content) VALUES (?)", (template,))
    conn.commit()
    conn.close()
