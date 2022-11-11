import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(100,90),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))

cv2.putText(img,"Mercury",(120,170),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"venus",(190,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Earth",(280,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mars",(380,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Jupiter",(460,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(730,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Uranus",(960,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune",(1110,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))



cv2.imshow("solar-planets",img)


cv2.waitKey(0)