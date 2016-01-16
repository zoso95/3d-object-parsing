import os 
import os.path
import random
import shutil
import time
import subprocess


MOVIE_DIR = "/home/gb/hackathon.mp4"
PICTURE_DIR = "/home/gb/parsed_pics/"
OUTPUT_DIR = "/home/gb/outputs"


BUNDLER_DIR = "/home/gb/osm-bundler/RunBundler.py"
BUNDLE_EXE = "/home/gb/osm-bundler/software/bundler/bin/bundler"
PMVS_DIR = "/home/gb/osm-bundler-master/RunPMVS.py"

RATE = "5"



def main():
	
	os.chdir(PICTURE_DIR)
	print "Calling: " + ' '.join(["ffmpeg", "-i", MOVIE_DIR,
					 "-r", RATE, "parsed_%05d.jpg"])
	subprocess.call(["ffmpeg", "-i", MOVIE_DIR,
					 "-r", RATE, "parsed_%05d.jpg"])
	

	
	os.chdir(PICTURE_DIR)
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			os.rename(name, str(('%06x' % random.randrange(16**6)).upper()) +".jpg")

	
	print "Calling: " +  ' '.join(["python", BUNDLER_DIR, "--photos="+PICTURE_DIR])
	subprocess.call(["python", BUNDLER_DIR, "--photos="+PICTURE_DIR, "--featureExtractor=siftlowe"])


	bundle_out = get_bundler_tmp_dir()

	
	append_camera(bundle_out)
	print "Reruning the bundle"
	
	subprocess.call([BUNDLE_EXE, os.path.join(bundle_out, "list.txt"),
					 "--options_file="+os.path.join(bundle_out, "options.txt")])
	
	
	print "Temp dir: " + bundle_out
	print "Calling: " + ' '.join(["python", PMVS_DIR, "--bundlerOutputPath="+bundle_out])
	subprocess.call(["python", PMVS_DIR, "--bundlerOutputPath="+bundle_out])

	move_all_files(bundle_out, "ply")
	
	

def get_bundler_tmp_dir():
	newest = ''
	mod_time = 0
	for child in os.walk("/tmp/"):
		name = child[0]
		if "osm-bundler" not in name or any([c in name for c in ["/pmvs", "/bundle"]]):
			continue
		last_modified = time.ctime(os.path.getmtime(name))
		if last_modified > mod_time:
			mod_time = last_modified
			newest = name
	if os.path.isdir(os.path.join(newest, "pmvs")):
		shutil.rmtree(os.path.join(newest, "pmvs"))
	return newest

def move_all_files(root, extension):
	for root, dirs, files in os.walk(root):
		for f in files:
			if extension in f:
				out_path = os.path.join(OUTPUT_DIR, f)
				in_path =  os.path.join(root, f)
				print "Copying "+in_path+" to "+ out_path
				open(out_path, 'a').close()
				shutil.copy(in_path, out_path)

def append_camera(out_dir):
	print("Trying to open " + os.path.join(out_dir, "list.txt"))
	with open(os.path.join(out_dir, "list.txt"), "r+") as f:
		s = []
		for line in f:
			# 2710, 10
			s.append(line.rstrip().split(' ')[0] + " 0 2700.000")
		f.seek(0)
		f.write("\n".join(s))
		f.truncate()


if __name__ == "__main__":
    main()
