import cv2

print('Package imported')

# Loading images
img = cv2.imread('/home/nachiket/Pictures/lofi-anime/img.jpg')
cv2.imshow('Output', img)
cv2.waitKey(0)
  
# Loading videos
vid = cv2.VideoCapture('/home/nachiket/Videos/snake-ai.webm')

while True:
    success, img = vid.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Loading webcam
vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)
vid.set(10, 100)

while True:
    success, img = vid.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
