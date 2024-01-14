import cv2
import mediapipe
from cvzone.HandTrackingModule import HandDetector
import socket
#Parameters
width, height = 1280, 720


#Webcam
cap =cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#Hand Detector
detector = HandDetector(maxHands=1,detectionCon=0.8)



while True:
    #Get the frame from webcam
    success, img = cap.read()
    #Hands
    hands, img =detector.findHands(img)



    cv2.imshow("Image",img)
    cv2.waitKey(1)

