import os
import cv2

DirPath = '.\Frames'
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)
    image = cv2.imread (imgPath, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', image)
    cv2.waitKey(5000)
    
cv2.destroyAllWindows()