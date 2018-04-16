import cv2
import argparse
import os,errno
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input video to extarct frames")

args = vars(ap.parse_args())

video_name = os.path.basename(args['input'])[:-4]
directory = os.path.dirname(args['input'])
if not directory == '':
	directory = directory+"/"
print(args['input'],video_name,directory)
frame_nums = []
with open(directory+"scenes.csv") as fp:
    for i, line in enumerate(fp):
        if i >= 2:
            # read from 3rd line
            frame_nums.append(int(line.split(',')[1]))
print(frame_nums)

cap = cv2.VideoCapture(args['input'])

shutil.rmtree(directory+"scd_ocr", ignore_errors=True)
for frame_no in frame_nums:
	cap.set(1,frame_no)
	success,image = cap.read()
	try:
		os.makedirs(directory+"scd_ocr")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	img_file = video_name+'_frame_'+str(frame_no)+'.jpg'
	img_path = directory+"scd_ocr/"+img_file
	cv2.imwrite(img_path,image)
	os.system("python ocr.py -i "+img_path+" > "+directory+"scd_ocr/ocr_op_"+img_file+".txt")	