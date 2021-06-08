import cv2

# Remember : 640x480 = 640 right and 480 down from top left corner

img = cv2.imread('./img.jpg')
print(img.shape)

# Resize
img_resize = cv2.resize(img, (300, 200))
print(img_resize.shape)

# Cropping convention :[height][width][channels]
img_cropped = img[0:200,200:500]

cv2.imshow('Image', img)
cv2.imshow('Image resized', img_resize)
cv2.imshow('Image cropped', img_cropped)
cv2.waitKey(0)
