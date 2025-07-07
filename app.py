from flask import Flask, render_template, redirect, send_file
import sqlite3
import pandas as pd
from datetime import datetime
import face_recognition
import cv2
import os

app = Flask(__name__)
DATABASE = 'database.db'
CSV_FILE = 'attendance.csv'

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/mark')
def mark_attendance():
    from face_recognition import mark_attendance_with_face_recognition
    mark_attendance_with_face_recognition()
    return redirect('/')

@app.route('/export')
def export_csv():
    return send_file(CSV_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)