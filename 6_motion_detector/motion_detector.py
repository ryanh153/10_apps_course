import cv2
from datetime import datetime
import pandas


threshold = 50
min_area = 10000

first_frame = None
video = cv2.VideoCapture(0)
status_list = []
status_changes = []
df = pandas.DataFrame(columns=["Start", "End"])

while True:
    status = 0
    frame = video.read()[1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, threshold, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for contour in contours:
        if cv2.contourArea(contour) < min_area:
            continue

        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            status_changes.append(datetime.now())
        break

    status_list.append(status)
    if len(status_list) > 2:
        status_list = status_list[-2::]
        if status_list[-1] != status_list[-2]:
            status_changes.append(datetime.now())

video.release()
cv2.destroyAllWindows

for i in range(0, len(status_changes), 2):
    df = df.append({"Start": status_changes[i], "End": status_changes[i+1]}, ignore_index=True)

df.to_csv("Times.csv")