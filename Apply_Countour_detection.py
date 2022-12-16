import os
import cv2
import numpy as np

DirPath = '.\Frames'
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)
    gray = cv2.imread (imgPath)
    # Apply a Gaussian blur to the image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Use the Canny edge detector to detect the edges in the image
    edges = cv2.Canny(blurred, 50, 150)
    # Find the contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Create a mask image with white pixels representing the foreground
    mask = 255 * np.ones(gray.shape, dtype=np.uint8)
    # Draw the contours on the mask image
    cv2.drawContours(mask, contours, -1, (0, 0, 0), -1)
    # Separate the foreground from the background using the mask
    foreground = cv2.bitwise_and(gray, mask)
    cv2.imshow('image', gray)
    cv2.imshow('foreground.jpg', foreground)
    cv2.waitKey(100)
    
cv2.destroyAllWindows()
