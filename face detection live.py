import cv2
from twilio.rest import Client

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Your WhatsApp phone number and Twilio phone number
whatsapp_number = 'your contact'
twilio_number = 'twilio contact'

def sendMsg(count):
    # Create a Twilio client object
    client = Client(account_sid, auth_token)

    # Send a message containing the count to your WhatsApp number
    message = client.messages.create(
        body=f'There are {count} people in the video.',
        from_=twilio_number,
        to=whatsapp_number
    )

    # Print the message SID
    print(message.sid)



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
		sendMsg(len(faces))
	elif cv2.waitKey(0) & 0xFF == ord('x'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
