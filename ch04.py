import cv2
import numpy as np

# drawing shapes

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# img[:] = 255, 0, 0 # full blue image

# Diagonal line from top left to bottom right
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# Circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# Inserting text on image
cv2.putText(img, "Nachiket", (300, 200), cv2.FONT_ITALIC, 1, (0, 150, 0), 1)


cv2.imshow('Image', img)
cv2.waitKey(0)
