import cv2
import os 
import numpy as np

#-----------#-----------------#----------------------@-----------------
                           # Images from video
#-----------#-----------------#----------------------@-----------------


cap = cv2.VideoCapture(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\video-2.mp4")
c = 0
while True:
    n,frame = cap.read()
    if n == True:
        file_name=r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\photo" + str(c) + ".png"
        cv2.imwrite(file_name,frame)
        cv2.imshow("Journey",frame)
        if cv2.waitKey(5) & 0xff == ord("k"):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()


#_______...-------->>> Check the Frame Rate of the Video

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS (Frames per second): {fps}")


## Cropped image

img = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
cropped_image = img[1600:2040,520:1250]
cv2.imshow("Crooped_image",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# -----------#-----------------#----------------------@-----------------
#                            Threshold 
# -----------#-----------------#----------------------@-----------------


img_for_binary = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg")
img_for_adaptive = cv2.imread(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Dipanshu.jpg",0)
cropped_image_binary = img_for_binary[1600:2040,520:1250]
cropped_image_adaptive = img_for_adaptive[1600:2040,520:1250]
ret, otsu_img = cv2.threshold(cropped_image_adaptive, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret,thresh_img = cv2.threshold(cropped_image_binary,127,255,cv2.THRESH_BINARY)
adathresh = cv2.adaptiveThreshold(cropped_image_adaptive,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Binary",thresh_img)
cv2.imshow("Adaptive",adathresh)
cv2.imshow("Otsu's Thresholding",otsu_img)

# success =  cv2.imwrite(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\throshold.jpg",_img)
success2 =  cv2.imwrite(r"C:\Users\DIPANSHU\OneDrive\Documents\OpenCV-photos\Ostu.jpg",otsu_img)
if success2:
    print("Images saved successfully.")
else:
    print("Images saving failed.")

cv2.waitKey(0)
cv2.destroyAllWindows()



#-----------#-----------------#----------------------@-----------------
#                        #   Mouse Event
#-----------#-----------------#----------------------@-----------------

def photo(event,x,y,f,p):
    if event ==cv2.EVENT_LBUTTONUP:
        cv2.circle(white_image,(x,y),5,(255,0,0),thickness=2)

    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(white_image,(x,y),(x+25,y+25),(0,255,0),thickness=2)

    elif event == cv2.EVENT_MOUSEMOVE and (f & cv2.EVENT_FLAG_LBUTTON):
        cv2.circle(white_image, (x, y), 5, (0, 0, 255), -1)


white_image = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.namedWindow("Mount")
cv2.setMouseCallback("Mount",photo)

while True:
    cv2.imshow('White Image', white_image)
    if  cv2.waitKey(1) % 0xFF == ord("k"):
        break

cv2.destroyAllWindows()
