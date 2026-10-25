#read a image
"""import cv2
img = cv2.imread("Resources/Image_1.png")
cv2.imshow("Mihir",img)
cv2.waitKey(0)"""

"""#read a video
import cv2

cap = cv2.VideoCapture("Resources/Video_1.webm")

while True:
    success, img = cap.read()
    
    
    if not success:
        print("End of video or failed to read frame.")
        break
        
    cv2.imshow("Terminal", img)
    
    if cv2.waitKey() & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""

"""#read a webcam and perform canny edge detection and dilation and erosion
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    
    if not success:
        print("End of video or failed to read frame.")
        break
    imgCanny = cv2.Canny(img, 100, 100)
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
    cv2.imshow("Terminal", imgEroded)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""

"""#Basic operations on images
import cv2
img = cv2.imread("Resources/Image_1.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)"""