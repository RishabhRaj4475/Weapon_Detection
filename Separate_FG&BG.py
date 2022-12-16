import numpy as np
import cv2 as cv
import os as os

DirPath = '.\Frames'
Frames = os.listdir(DirPath)

for Frame in Frames:
    
    if Frame :
        break
    imgPath = os.path.join(DirPath , Frame)
    print("The image file is :" , imgPath)
    
    image = cv.imread(imgPath, )
    
    #removing the background from the image to get the foreground
    #kernel = cv.getStructuringElement (cv.MORPH ELLIPSE, (3,3))
    fgbg = cv.createBackgroundSubtractorKNN()
    
    fgmask = fgbg.apply(image)
    #fgmask = cv.morphologyEx (fgmask, CV. MORPH OPEN, kernel)
    #cv.imshow('FG MASK Frame', fgmask)
    keyboard = cv.waitKey (30)
    if keyboard == 'q' or keyboard == 27:
        break


cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)
    keyboard = cv.waitKey (30)
    if keyboard == 'q' or keyboard == 27:
        break
cap. release ()
cv.destroyAllWindows ()