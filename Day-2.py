
##-----------#-----------------#----------------------@-----------------
##                   Text,lines,rectangle,circle and ellipse  on images
##-----------#-----------------#----------------------@-----------------

import cv2
import os
import numpy as np


img1 = cv2.imread(r"C:\\Users\\DIPANSHU\\OneDrive\\Pictures\Screenshots 1\Screenshot 2024-12-24 163243.png")
old_img2 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Pictures\Screenshots 1\Screenshot 2024-12-24 163243.png",0)
img2 = cv2.cvtColor(old_img2,cv2.COLOR_GRAY2BGR)

cv2.putText(img1,
            text = "Dipanshu Choudhary",
            org=(20,100),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color = (0,255,0),
            thickness=2,
            lineType=cv2.LINE_AA
)

cv2.putText(img2,
            text = "Dipanshu Choudhary",
            org=(20,100),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color = (0,255,0),
            thickness=2,
            lineType=cv2.LINE_AA
)

new_img1 = cv2.rectangle(img1 , pt1=(60,140),pt2=(280,450),color=(255,0,0),thickness=2)
new_img2 = cv2.rectangle(img2,pt1=(60,130),pt2 = (285,445),color =(255,0,0),thickness = 2)
hsort = np.hstack((new_img1,new_img2))

cv2.imshow('Image',hsort)
cv2.waitKey(0)


-------------->>>> For circle 
cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)


--------------->>>> for ellipse
cv2.ellipse(img, center, axes, angle(ACW), startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
