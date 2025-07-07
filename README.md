# 📸 Smart Attendance System using Face Recognition

A lightweight web-based application that uses facial recognition to automate attendance marking in classrooms or office environments. Built using Python, OpenCV, Flask, and SQLite.

---

## 🛠 Tech Stack

- Python 3.8–3.10 (⚠️ Not compatible with Python 3.12+ for `dlib`)
- OpenCV (`cv2`)
- face_recognition
- Flask (for the web interface)
- SQLite (for attendance logs)
- Pandas (for CSV export)

---

## 🎯 Features

✅ Real-time face recognition using webcam  
✅ Timestamp logging and SQLite database storage  
✅ Simple and clean Flask UI dashboard  
✅ CSV export of attendance records  
✅ Easy to set up and run locally

---

## 📁 Folder Structure
smart_attendance_system/
├── app.py # Flask application
├── face_recognition.py # Facial recognition logic
├── attendance.csv # CSV log of attendance
├── database.db # SQLite DB for persistence
├── requirements.txt
├── static/
│ └── style.css # Dashboard styling
├── templates/
│ └── index.html # Flask dashboard
└── dataset/ # Folder containing student face images
