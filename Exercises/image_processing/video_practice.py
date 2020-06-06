import cv2

video = cv2.VideoCapture("video.mp4")

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break