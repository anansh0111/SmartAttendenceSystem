
import cv2
import numpy as np
import face_recognition
import os
import sqlite3
from datetime import datetime
import pandas as pd

path = 'dataset'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS attendance (name TEXT, time TEXT)''')
conn.commit()
conn.close()


def mark_attendance_with_face_recognition():
    cap = cv2.VideoCapture(0)
    marked = set()

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                if name not in marked:
                    marked.add(name)
                    now = datetime.now()
                    dtString = now.strftime('%Y-%m-%d %H:%M:%S')

                    conn = sqlite3.connect('database.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO attendance (name, time) VALUES (?, ?)", (name, dtString))
                    conn.commit()
                    conn.close()

                    # Also save to CSV
                    df = pd.DataFrame([[name, dtString]], columns=['Name', 'Time'])
                    if os.path.exists('attendance.csv'):
                        df.to_csv('attendance.csv', mode='a', header=False, index=False)
                    else:
                        df.to_csv('attendance.csv', index=False)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()