import numpy as np
import cv2
import pyttsx3
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def calling():
    #time.sleep(2)
    engine = pyttsx3.init()
    engine.say("Hey There")
    engine.runAndWait()

cap = cv2.VideoCapture(0)
i=1

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y: y +h, x: x +w]
        roi_color = img[y: y +h, x: x +w]

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Hey There!', (0, 130), font, 1, (0, 0, 0), 2, cv2.LINE_AA)


        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex ,ey ,ew ,eh) in eyes:
            cv2.rectangle(roi_color ,(ex ,ey) ,(ex +ew ,ey +eh) ,(0 ,255 ,0) ,2)

        if i==1:
            calling()

        i=0

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()