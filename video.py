import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# 0 first webcam, 1 second webcam, 0 is standard webcam
cap = cv2.VideoCapture(1)

while True:
    # if there is a feed return
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)

    cv2.imshow('frame', frame)
    # if key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# stopping camera after
cap.release()
cv2.destroyAllWindows()
