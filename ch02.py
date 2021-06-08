import cv2
import numpy as np

img = cv2.imread('./img.jpg')
h, w, c = img.shape
print(f'Image Shape = {h}, {w}, {c}')

def display(img):
    cv2.imshow('my_image', img)
    while True:
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break 

# Creating gray images
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
display(img_gray)

# Creating blur images -> (7, 7) is kernel size (usually odd)
img_blur = cv2.GaussianBlur(img, (7, 7), 0)
display(img_blur)

# Edge detector
img_canny = cv2.Canny(img, 100, 100)
display(img_canny)

# Image dilation
kernel = np.ones((5, 5), np.uint8)
img_dilate = cv2.dilate(img_canny, kernel, iterations = 2)
display(img_dilate)

# Image erotion
img_erode = cv2.erode(img_dilate, kernel, iterations = 1)
display(img_erode)
