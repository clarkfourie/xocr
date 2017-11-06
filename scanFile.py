# writes OCR content from an image to a text file

import io
from google.cloud import vision
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

img_pwd = filedialog.askopenfilename(initialdir = 'C:/Sage/X3PEOPLE/folders/SEED/PIC') # select image
file_pwd = 'C:\Users\Administrator\Desktop\cloudstuff\\newtxt.txt' # write content to

client = vision.Client()


with io.open(img_pwd, 'rb') as image_file:
	image = client.image(content=image_file.read())

file = open(file_pwd,'w')

texts = image.detect_text()
for text in texts:
	print (text.description.encode('ascii', 'ignore').decode('ascii'))
	file.write(text.description.encode('ascii', 'ignore').decode('ascii'))

file.close()