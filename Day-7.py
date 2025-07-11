# -----------#-----------------#----------------------@-----------------
#                            Corner Detection 
# -----------#-----------------#----------------------@-----------------

import cv2
import numpy as np
import os

# (Harris Corner Detection)

img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dippu.jpg")
img = cv2.resize(img,(800,600))
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
gr = np.float32(gr)
res = cv2.cornerHarris(gr,10,3,0.05)
res = cv2.dilate(res,None)

img[res>0.01*res.max()] = [0,0,255]

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#(Shi-Tomasi Corner Detectio)

img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
img = cv2.resize(img,(800,600))
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

item = cv2.goodFeaturesToTrack(gr,12,0.02,5)
item = np.int64(item)

for i in item:
    x,y = i.ravel()
    cv2.circle(img,(x,y),5,(0,255,0),-1)

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Contour Detection & Drawing


import cv2

img = cv2.imread("path/to/image.jpg")
img = cv2.resize(img, (800, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -----------#-----------------#----------------------@-----------------
#                            Face Detection 
# -----------#-----------------#----------------------@-----------------



# Get path to Haar cascade folder
haar_path = cv2.data.haarcascades
print("Haar cascade directory:", haar_path)



img1  = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\best.jpg")
img = cv2.resize(img1,(800,600))
gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

fade = cv2.CascadeClassifier(r"C:\Users\DIPANSHU\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
dect = fade.detectMultiScale(gry,1.1,4)

for (x,y,w,h) in dect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
