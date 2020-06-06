import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

for face in faces:
    x, y, w, h = face
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))

cv2.imshow("Im", img)
cv2.waitKey(0)
