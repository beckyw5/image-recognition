import numpy as np
import cv2

# 0 first webcam, 1 second webcam, 0 is standard webcam
cap = cv2.VideoCapture(0)
while True:
    # if there is a feed return
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

