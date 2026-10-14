import sqlite3
from datetime import datetime

DB_NAME = "stress_records.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            semester INTEGER NOT NULL,
            date TEXT NOT NULL,
            percentage REAL NOT NULL,
            level TEXT NOT NULL,
            highest_category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def check_student_exists(student_name):
    
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
  
    cursor.execute("SELECT COUNT(*) FROM records WHERE LOWER(student_name) = LOWER(?)", (student_name.strip(),))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def save_record(student_name, semester, percentage, level, highest_category):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO records (student_name, semester, date, percentage, level, highest_category)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_name.strip(), semester, date_str, percentage, level, highest_category))
    conn.commit()
    conn.close()

def get_all_records():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT student_name, semester, date, percentage, level, highest_category FROM records ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows