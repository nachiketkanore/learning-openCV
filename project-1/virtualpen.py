import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Colors mask h, s, v (min, max) colors 
# found using controller
myColors = [
    [5, 107, 0, 19, 255, 255], # Orange
    [133, 56, 0, 159, 156, 255],
    [57, 76, 0, 100, 255, 255]
]
# BGR format for corresponding myColors
myColorValues = [
    [51, 153, 255],
    [255, 0, 255],
    [0, 255, 0]
]

# (x, y, which_color)
myPoints = [

]

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    
    for color in myColors:
        lower = np.array(color[0:3]) 
        upper = np.array(color[3:6]) 
        mask = cv2.inRange(imgHSV, lower, upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1

    return newPoints

    # cv2.imshow('mask', mask)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            # finding curve length
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def drawOnCanvas(myPoints, myColorValues):
    for x, y, idx in myPoints:
        cv2.circle(imgResult, (x, y), 10, myColorValues[idx], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img)

    if len(newPoints) != 0:
        for newpoint in newPoints:
            myPoints.append(newpoint)
    
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)


    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
