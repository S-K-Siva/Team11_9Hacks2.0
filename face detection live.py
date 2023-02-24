import cv2
count = 0

video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	
	# Display the resulting frame
	cv2.putText(frame,f'Count:{len(faces)}',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()