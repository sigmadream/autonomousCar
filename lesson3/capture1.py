import time
import cv2

c = cv2.VideoCapture(0) 
time.sleep(0.1)
 
while(True):
    _,image = c.read()

    cv2.imshow("Frame", image)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()