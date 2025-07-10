# -----------#-----------------#----------------------@-----------------
#                            Contours
# -----------#-----------------#----------------------@-----------------

img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\best.jpg")
gry  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
re_img = cv2.resize(gry,(800,600))
_,thresh = cv2.threshold(gry,120,255,cv2.THRESH_BINARY)

cont,hie = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(re_img,cont,-1,(0,255,0),2)
cv2.imshow("Trip",re_img)

# cv2.arcLength(cnt,True)
# x,y,w,h = cv2.boundingRect(cnt)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Step 1: Read and Preprocess
img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\best.jpg")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
re_img = cv2.resize(gry, (800, 600))
_, thresh = cv2.threshold(re_img, 130, 255, cv2.THRESH_BINARY)

# Step 2: Find contours
contours, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 3: Convert grayscale to color for drawing
output = cv2.cvtColor(re_img, cv2.COLOR_GRAY2BGR)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:  # Filter noise by area threshold
        perimeter = cv2.arcLength(cnt, True)

        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(cnt)

        # Draw contour
        cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)

        # Draw bounding box
        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Step 5: Show final result
cv2.imshow("Photo", output)
cv2.waitKey(0)
cv2.destroyAllWindows()




# -----------#-----------------#----------------------@-----------------
#                            grabcut
# -----------#-----------------#----------------------@-----------------


img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\best.jpg")
mask = np.zeros(img.shape[:2],np.uint8)

bgmask = np.zeros((1,65),np.float64)*255
fgmask = np.zeros((1,65),np.float64)*255
dim = (50,68,100,120)

cv2.grabCut(img,mask,dim,bgmask,fgmask,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask ==2) | (mask == 0),0,1).astype("uint8")
img = img*mask2[:,:,np.newaxis]

cv2.imshow("hh",img)
cv2.waitKey(0)
cv2.destroyAllWindows()