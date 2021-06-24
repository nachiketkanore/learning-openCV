# Number plate detection - bounding box prediction
import cv2
import numpy as np
from stackImages import stackImages

frameWidth = 640
frameHeight = 480
minArea = 500
color = (255, 0, 255)
noPlateCascade = cv2.CascadeClassifier('./haarcascade_russian_plate_number.xml')

img = cv2.imread('./vehicles.jpg')

saved = 0

while True:
    imgOrig = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    noPlates = noPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in noPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(img, 'Number plate', (x, y-5), 
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgROI = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgROI)

    outputImg = stackImages(0.6, ([imgOrig], [img]))
    cv2.imshow('Image', outputImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    saved += 1

    if saved == 21:
        cv2.imwrite('./outputs.jpg', outputImg)
