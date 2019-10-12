import cv2
import numpy as np
import pyzbar.pyzbar as pz

def Qrscan():
	cap=cv2.VideoCapture(0)
	font=cv2.FONT_HERSHEY_PLAIN
	x=0
	while True:
		_,frame = cap.read()
		decodedObjects=pz.decode(frame)
		for obj in decodedObjects:
			returnQr=obj.data
			print(returnQr)
			exit(0)
		#cv2.putText(obj.data)
		#cv2.putText(frame,str(obj.data),(50,50),font,3,(255,0,0),3)
		cv2.imshow( "Frame",frame)
		key=cv2.waitKey(1)
		if key==27:
			break
		x+=1

#Qrscan()

