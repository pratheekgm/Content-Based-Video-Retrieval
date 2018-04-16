import os,errno
import argparse
from glob import glob
import shutil

ap = argparse.ArgumentParser()

# ap.add_argument("-i", "--input", required=True,
# 	help="path to input video to extarct frames")

ap.add_argument("-t", "--thresh", default=5,
 	help="threshold for delta_avg_hsv")

args = vars(ap.parse_args())
video_type = "mp4"
vids = [os.path.basename(i) for i in glob("*."+video_type)]
print(vids)
for vid in vids:
	shutil.rmtree("./"+vid[:-4], ignore_errors=True)
	try:
		os.makedirs(vid[:-4])
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	os.system("scenedetect -i "+vid+" -d content -s stats.csv -t "+args['thresh']+" -df 4 -co scenes.csv")
	os.system("python scd.py -i "+vid)
	os.system("python thumbs.py -i "+vid)
	shutil.move(vid,vid[:-4]+"/"+vid)
	shutil.move("stats.csv",vid[:-4]+"/stats.csv")
	shutil.move("scenes.csv",vid[:-4]+"/scenes.csv")
	shutil.move("scd_ocr",vid[:-4]+"/scd_ocr")
	shutil.move("thumb.jpg",vid[:-4]+"/thumb.jpg")
	shutil.move("poster.jpg",vid[:-4]+"/poster.jpg")

# folders = glob("*/")
# for folder in folders:
# 	os.system("python scd.py -i "+folder+folder[:-1]+"."+video_type)

# frames = [os.path.basename(i) for i in glob.glob("*.jpg")]

# for frame in frames:
# 	os.system("python ocr.py -i "+frame+" > ocr_op"+frame[len(args['input'].split('.')[0]):-4]+".txt")


