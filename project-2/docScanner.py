# Document scanner and enhancer
import cv2
import numpy as np
from stackImages import stackImages

widthImg, heightImg = 640, 480

path = './img.jpg'
img = cv2.imread(path)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    biggest = np.array([])
    maxArea = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 8)
            # finding curve length
            peri = cv2.arcLength(cnt, True)

            # Approx polygon for our contour
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(area, len(approx))
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    # border contours printing in different image
    cv2.drawContours(imgBorder, biggest, -1, (0, 0, 255), 18)
    return biggest

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    # cv2.imshow('Canny image', imgCanny)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations = 2)
    imgThresh = cv2.erode(imgDial, kernel, iterations = 1)
    
    return imgThresh

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def getWarp(img, biggest):

    biggest = reorder(biggest)
    print(biggest.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    
    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))
    return imgCropped

saved = False

while True:
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgBorder = img.copy()

    imgThresh = preProcessing(img)
    biggest = getContours(imgThresh)

    if len(biggest) < 4:
        print('No contours found')
        exit(0)
    
    cv2.drawContours(imgBorder, biggest, -1, (255, 0, 0), 18)
    
    imgWarped = getWarp(img, biggest)

    imgStack = stackImages(0.4, ([img, imgThresh], [imgBorder, imgWarped]))
    cv2.imshow('Application', imgStack)

    if not saved:
        saved = True
        cv2.imwrite('./output.jpg', imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
