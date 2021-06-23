import cv2
import numpy as np

# Face Detection
# Positive faces + Negative faces ---> Train ---> XML file (dataset)
# We will not train, use pretrained file --> openCV cascades

# Explore more cascade in openCV (also custom cascade)

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

img = cv2.imread('./faces.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow('Result', img)
cv2.waitKey(0)
