"""
Haq - Database Module
"""

import sqlite3
from datetime import datetime
import hashlib

DB_NAME = "haq_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            phone TEXT,
            message TEXT,
            platform TEXT,
            result TEXT,
            confidence INTEGER,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password_hash TEXT
        )
    ''')
    
    cursor.execute("SELECT * FROM admin")
    if not cursor.fetchone():
        password_hash = hashlib.sha256("Haq2026".encode()).hexdigest()
        cursor.execute("INSERT INTO admin (username, password_hash) VALUES (?, ?)", 
                       ("admin", password_hash))
    
    conn.commit()
    conn.close()
    print("✅ Database initialized")

def save_search(ip, phone, message, platform, result, confidence):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO searches (ip, phone, message, platform, result, confidence, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ip, phone, message, platform, result, confidence, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()

def get_all_searches(limit=100):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT ip, phone, message, platform, result, confidence, created_at 
        FROM searches 
        ORDER BY id DESC 
        LIMIT ?
    ''', (limit,))
    
    data = cursor.fetchall()
    conn.close()
    return data

def verify_admin(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM admin WHERE username = ? AND password_hash = ?", 
                   (username, password_hash))
    
    result = cursor.fetchone()
    conn.close()
    return result is not None
