import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, img = cap.read()
if ret:
    cap.release()
    cv2.imshow('input_image', img)
    cv2.imwrite('input.png', img)
    img_gray = cv2.imread('input.png', 0)
    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    height = img_gray.shape[0]
    width = img_gray.shape[1]
    img_gray = cv2.line(img_gray,(0,0),(width, height),(255,0,0),5)
    img_gray = cv2.rectangle(img_gray, (width//2, 0), (width - 1, 128), (0, 255, 0), 1)
    cv2.imshow('grey_image', img_gray)
    cv2.waitKey(0)
else:
    print("There is some error with your camera\n")
cv2.destroyAllWindows()