from glob import glob
import cv2 
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input video")

args = vars(ap.parse_args())
size = (150,100)
#frames_path = os.getcwd()+"/frames"

vid = args["input"]
cap = cv2.VideoCapture(vid)
length = int(cap.get(7))
cap.set(1,length/10)
ret,frame = cap.read()
if ret:
	try:
		ret2 = cv2.imwrite("poster.jpg",frame)
		frame = cv2.imread("poster.jpg")
		resized_image = cv2.resize(frame, size)
		cv2.imwrite("thumb.jpg", resized_image)
		
	except Exception as e: 
		print(e)
else:
	print("cannot read frame")
