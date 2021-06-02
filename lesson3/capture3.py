import time
import cv2
import csv

 
c = cv2.VideoCapture(0)
time.sleep(0.1)
 
# capture frames from the camera
cnt = 0
f=open('./data/data.csv','w')
fwriter = csv.writer(f)

while(True):
    _,image = c.read()
    image = cv2.resize(image, (320,240))

    # show the frame
    cv2.imshow("Frame", image)

    myimage = time.strftime('%Y-%m-%d_%H:%M:%S') +'_' + str(cnt) + '.jpg'
    cv2.imwrite('./data/'+ myimage, image)

    fwriter.writerow((myimage, 1))

    key = cv2.waitKey(1)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    cnt += 1	
f.close()
cv2.destroyAllWindows()