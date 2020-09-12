import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
CADR_PER_SEC = 20
out = cv2.VideoWriter('input_video.mp4', fourcc, CADR_PER_SEC,  (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        out.write(frame)

        cv2.imshow('input_video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Something went wrong\n")
        break

cap.release()
out.release()

cap = cv2.VideoCapture('input_video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        height = frame.shape[0]
        width = frame.shape[1]
        frame = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)
        frame = cv2.rectangle(frame, (width // 2, 0), (width - 1, 128), (0, 255, 0), 1)

        cv2.imshow('gray_video', frame)
        if cv2.waitKey(1000//CADR_PER_SEC) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()