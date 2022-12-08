import cv2

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
i = 0

while(cap.isOpened()):
	ret, frame = cap.read()
	
	# This condition prevents from infinite looping
	# incase video ends.
	if ret == False:
		break


	# convert the captured frame into grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Save Frame by Frame into disk using imwrite method
	cv2.imwrite('/Users/risha/Desktop/major project/Frames/Frame'+str(i)+'.jpg', gray)
	i += 1

cap.release()
cv2.destroyAllWindows()
