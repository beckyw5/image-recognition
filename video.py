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
        # roi region of interest
        roi_grey = grey[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_grey)

        color = (255, 0, 0)
        stroke = 2
        end_coordinate_x = x + w
        end_coordinate_y = y + h
        cv2.rectangle(frame, (x, y), (end_coordinate_x , end_coordinate_y), color, stroke)

    cv2.imshow('frame', frame)
    # if key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# stopping camera after
cap.release()
cv2.destroyAllWindows()
