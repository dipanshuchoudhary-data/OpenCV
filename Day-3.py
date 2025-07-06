import cv2
import os
import numpy


# -----------#-----------------#----------------------@-----------------
#                            Merge of images
# -----------#-----------------#----------------------@-----------------


img1 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
img2 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\J&K1.jpg")

img1 = cv2.resize(img1,(700,800))
img2 = cv2.resize(img2,(700,800))

# new_img1 = cv2.addWeighted(img1,0.7,img2,0.9,1.0)

new_img2 = cv2.subtract(img2,img1)

cv2.imshow("Adding",new_img1)
cv2.imshow("Substract",new_img2)
cv2.waitKey(0)



# -----------#-----------------#----------------------@-----------------
#                            Edge Detection and saving a image
# -----------#-----------------#----------------------@-----------------


img1 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
img1 = cv2.resize(img1,(600,700))
new_img = cv2.Canny(img1,120,120,L2gradient=True)
# cv2.imshow("Dippu",new_img)
# cv2.waitKey(0)
success =  cv2.imwrite(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Edge.jpg",new_img)
if success:
    print("Image saved successfully.")
else:
    print("Image saving failed.")




# -----------#-----------------#----------------------@-----------------
#                            Blur image
# -----------#-----------------#----------------------@-----------------


# Read and resize the image
img1 = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
img1 = cv2.resize(img1, (600, 700))

# 1. Average Blurring
avg_blur = cv2.blur(img1, (5, 5))

# 2. Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(img1, (5, 5), 0)

# 3. Median Blurring
median_blur = cv2.medianBlur(img1, 5)

# Display all images
cv2.imshow("Original Image", img1)
cv2.imshow("Average Blur", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()