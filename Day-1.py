
import cv2
import numpy as np

#-----------#-----------------#----------------------@-----------------
                           # Grayscale image to color and vica versa
#-----------#-----------------#----------------------@-----------------


img1 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Pictures\Screenshots 1\Screenshot 2024-12-24 163243.png",0)
img2= cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Pictures\Screenshots 1\Screenshot 2024-12-24 163243.png")
re_img1 = cv2.resize(img1,(400,600))
re_img2 = cv2.resize(img2,(400,600))

re_img1_color = cv2.cvtColor(re_img1,cv2.COLOR_GRAY2BGR)

hsorting = np.hstack((re_img1_color,re_img2))
cv2.imshow("My image",hsorting)
cv2.waitKey(0)


import os



img1 = cv2.imread(r"C:\\Users\\DIPANSHU\\OneDrive\\Pictures\Screenshots 1\Screenshot 2024-12-24 163243.png")
img2 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Pictures\Screenshots 1\Screenshot 2024-12-24 163222.png")
re_img1 = cv2.resize(img1,(400,600))
re_img2 = cv2.resize(img2,(400,600))

merge = np.array([1,2,3,1,2,3])
hsort = np.hstack((re_img1,re_img2))
vsort = np.vstack((hsort,hsort))
print(merge)

cv2.imshow("Image",vsort)
cv2.waitKey(0)

# print(img) ----> Show img in the form of array (pixel values)
cv2.destroyAllWindows()


#-----------#-----------------#----------------------@-----------------
                           # Slideshow of images
#-----------#-----------------#----------------------@-----------------

list_dir = os.listdir(r"C:\Users\DIPANSHU\OneDrive\Pictures\Screenshots 1\New folder")
for name in list_dir:
    path = "C:\\Users\\DIPANSHU\\OneDrive\\Pictures\\Screenshots 1\\New folder"
    img_name = path+"\\"+name
    img = cv2.imread(img_name)
    img = cv2.resize(img,(500,500))
    cv2.imshow("Presentation",img)
    cv2.waitKey(0)
