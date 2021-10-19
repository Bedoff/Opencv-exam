import cv2
import time
import numpy as np

qs = 0.7 #eşleşme oranı

mainimage = cv2.imread("image.jpg")
pimage = cv2.cvtColor(mainimage,cv2.COLOR_BGR2GRAY)

a1 = cv2.imread("search/semsiye.png",0)
a2 = cv2.imread("search/yuvarlak.png",0)
a3 = cv2.imread("search/yildiz.png",0)
a4 = cv2.imread("search/ucgen.png",0)
a5 = cv2.imread("search/haha.png",0)
a6 = cv2.imread("search/pust.png",0)

def scan(image):
    w,h = image.shape[::-1]
    res = cv2.matchTemplate(pimage,image,cv2.TM_CCOEFF_NORMED)

    loc = np.where(res>qs)
    for n in zip(*loc[::-1]):
        cv2.rectangle(mainimage, n, (n[0]+w,n[1]+h), (124,252,0), 1)
        
          

def refreshpage():
    cv2.imshow("OpenCV",mainimage)
    cv2.waitKey(3000)


scan(a1)
refreshpage()
scan(a2)
refreshpage()
scan(a3)
refreshpage()
scan(a4)
refreshpage()
scan(a5)
scan(a6)


cv2.imshow("OpenCV",mainimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
