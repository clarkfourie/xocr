import io
from google.cloud import vision
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(initialdir = 'C:/Sage/X3PEOPLE/folders/SEED/PIC')

print('Connecting to Google Vision...')

vision_client = vision.Client()
img_path = file_path

print('Sending image: ' + img_path)

with io.open(img_path, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

# labels = image.detect_labels()
# for label in labels:
#     print(label.description)

passno = idno = ''
texts = image.detect_text()
#for text in texts:
#	print(text.description)

print('Extracting defined fields...')

index = 0
for index in range(len(texts)):
	if texts[index].description == 'SUD':
		passno = texts[index+1].description

	if texts[index].description == 'OCENTTE':
		idno = texts[index+1].description
	# print(i,' ',texts[index].description)
	# i += 1

# print(passno)
# print(idno)

file_name = 'C:\Sage\X3PEOPLE\\folders\SEED\PIC\ocrfile.txt' 

print('Writing to file: ' + file_name)

file = open(file_name,'w')

file.write(passno + ';')
file.write(idno)

file.close()