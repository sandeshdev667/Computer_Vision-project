import cv2
from range_file import get_limits

red = [0, 0, 255]  # BGR for red


cap = cv2.VideoCapture(0)
while True: 
    ret, frame = cap.read()

    hsvImage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(red)

    mask = cv2.inRange(hsvImage, (lowerLimit), (upperLimit))


    cv2.imshow('Red_Color_Detection   (Press "a" to quit)', mask)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()

cv2.destroyAllWindows()