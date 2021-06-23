# joining images
import cv2
import numpy as np

img = cv2.imread('img.jpg')

# horizontal stack
hor_img = np.hstack((img, img))
cv2.imshow('Horizontal join', hor_img)

# Vertical stack
ver_img = np.vstack((img, img))
cv2.imshow('Vertical join', ver_img)

cv2.waitKey(0)

