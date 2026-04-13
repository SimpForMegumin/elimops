from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def izveidot_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
      """ )
    conn.commit()
    conn.close()

izveidot_db()