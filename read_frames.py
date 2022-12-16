import cv2

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
index = 0

while(cap.isOpened()):
    ret, frame = cap.read()
	
	# This condition prevents from infinite looping
	# incase video ends.
    if ret == False:
        break

	# convert the captured frame into grayscale
	#1 method to do that
 	# -> gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#2 method to do that 
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #3rd method to do that and the best one in our aspect for pur project
    #gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
	
	# Save Frame by Frame into disk using imwrite method
    cv2.imwrite('/Users/risha/Desktop/major project/Frames/Frame'+str(index)+'.jpg', gray)
    index += 1

cap.release()
cv2.destroyAllWindows()
