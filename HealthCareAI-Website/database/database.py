import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'HealthCareAI.db')
UPLOAD_DIR = os.path.join(BASE_DIR, 'Uploaded')

print(f"[DB] Database path: {DB_PATH}")

def create_directories():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    print(f"[DB] Created upload directory: {UPLOAD_DIR}")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    print("[DB] Creating database tables...")
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL UNIQUE,
            EMAIL TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CONTACT(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            CONTACT TEXT,
            MESSAGE TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS NEWSLETTER(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EMAIL TEXT NOT NULL UNIQUE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PATIENTS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            PATIENT_ID TEXT,
            CONTACT TEXT,
            COUNTRY TEXT,
            STATE TEXT,
            PINCODE TEXT,
            GENDER TEXT,
            AGE INTEGER,
            DISEASE TEXT,
            RESULT TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("[DB] Database tables created successfully!")

if __name__ == '__main__':
    create_directories()
    init_database()