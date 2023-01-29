from PIL import Image
### 
# Notebook to run ocr on all of the images
###

import os
import pytesseract
from pytesseract import Output
import pandas as pd
from tqdm import tqdm
import cv2


def getFiles():
    files = os.listdir("./img")
    return files

files = getFiles()

for file in tqdm(files):
	fid = file.split(".")[0]

	orig = cv2.imread(f"img/{fid}.jpg")

	if orig is None:
		continue

	img = orig.copy()
	#img = Image.open(f"img/{fid}.jpg")

	df = pd.DataFrame()

	options = "--psm 4"
	text = pytesseract.image_to_string(
		cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
		config=options)
	
	if (text):
		df = pd.concat([df, pd.DataFrame([text])])

	df.to_csv("./new_ocr/" + fid + ".csv", index=False)


