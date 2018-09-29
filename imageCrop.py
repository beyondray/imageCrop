
import os
from PIL import Image

def imagesCrop(src, dest, box):
	fileIter = os.walk(src)
	for path,d,filelist in fileIter:  
	    for filename in filelist:
	        if (filename.endswith('jpg') or 
	        	filename.endswith('png') or
	        	filename.endswith('bmp')) :
	            imageCrop(path, filename, dest, box) 

def imageCrop(path, filename, outpath, box):
	filePath = os.path.join(path, filename)
	outFilePath = os.path.join(outpath, filename)
	img = Image.open(filePath)
	img.crop(box).save(outFilePath)
	print ("generate image in path: %s" % (outFilePath))

_SUCCESS = 1
_EMPTY 	= 0 
_FAIL 	= -1

def pathCheck(src):
	if os.path.exists(src):
		return _SUCCESS
	elif src == '':
		return _EMPTY
	else:
		return _FAIL

def pathSucCheck(src, canEmpty=False):
	res = pathCheck(src)
	is_success = res == _SUCCESS
	if canEmpty and res == _EMPTY:
		src = os.getcwd()
		is_success = True
	if not is_success:
		print("[Error}: the path: %s is not exist" % src)
	return is_success, src

def pathDirInput(prompt_key, canEmpty):
	while True: 
		src = input("please input the path of %s directory:" % (prompt_key))
		res, path = pathSucCheck(src, canEmpty)
		if res: return path

def filenameInput(path):
	while True:
		filename = input("please input the filename of image:") 
		src = os.path.join(path, filename)
		if pathSucCheck(src): return filename

def boxInput():
	box = input("please input x, y, w, h of image and split by ',':")
	arr = box.split(',')
	x, y, w, h = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])	
	return (x, y, x + w, y + h)

def main():
	mode = input("please input crop mode (batch, single):")

	if mode == 'batch' or mode == 'single':
		src = pathDirInput('src', False)
		dest = pathDirInput('dest', True)
		box = boxInput() 	#402, 149, 1100, 620
		if mode == 'single':
			filename = filenameInput(src)
			imageCrop(src, filename, dest, box) 
		else:
			imagesCrop(src, dest, box) 
	else:
		print("[Error]: the mode of %s is not exist!!" % mode)

if __name__ == "__main__":
	main()