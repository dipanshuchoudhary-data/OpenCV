import cv2
import numpy as np

# --------------------------- #
# 1. Video Playing from File  #
# --------------------------- #

cap = cv2.VideoCapture(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\video-2.mp4")
while cap.isOpened():
    n, frame = cap.read()
    if n is True:
        frame = cv2.resize(frame, (700, 1000))
        cv2.imshow("Journey", frame)
        if cv2.waitKey(40) & 0xff == ord("k"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


# -------------------------------- #
# 2. Video Playing Using Webcam    #
# -------------------------------- #

cap = cv2.VideoCapture(0)
while True:
    n, frame = cap.read()
    if n is True:
        frame = cv2.resize(frame, (600, 1200))
        cv2.imshow("Journey", frame)
        if cv2.waitKey(1) & 0xff == ord("k"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


# ----------------------------------------- #
# 3. Morphological Operations on an Image   #
# ----------------------------------------- #

img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg", 0)
img = cv2.resize(img, (600, 700))

# Convert to binary using thresholding
_, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# Define a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply Morphological Operations
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Display all results
cv2.imshow("Original Grayscale", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening (Erosion -> Dilation)", opening)
cv2.imshow("Closing (Dilation -> Erosion)", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()



## @@@@@@@@ note :-
##----->>>> cv2.pyrdown(img) --> use for shrink image. order/shape => Original → (1/2) → (1/4) → (1/8) ...
##----->>>> cv2.pyrUp(img) --> use for Scale or large image. order/shape => (1/8) → (1/4) → (1/2) → Original
