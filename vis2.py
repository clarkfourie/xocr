import io
from google.cloud import vision
import tkinter as tk
from tkinter import filedialog
# import sys

# print sys.stdout.encoding
# print u"Stöcker".encode(sys.stdout.encoding, errors='replace')
# print u"Стоескер".encode(sys.stdout.encoding, errors='replace')

# def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
#     enc = file.encoding
#     if enc == 'UTF-8':
#         print(*objects, sep=sep, end=end, file=file)
#     else:
#         f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
#         print(*map(f, objects), sep=sep, end=end, file=file)

# uprint('foo')
# uprint(u'Antonín Dvořák')
# uprint('foo', 'bar', u'Antonín Dvořák')


# import sys

# if sys.stdout.encoding != 'cp850':
#   sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
# if sys.stderr.encoding != 'cp850':
#   sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

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

# passno = idno = ''
texts = image.detect_text()
index = 0
for index in range(len(texts)):
	print(texts[index].description)

# print('Extracting defined fields...')

# index = 0
# for index in range(len(texts)):
# 	if texts[index].description == 'SUD':
# 		passno = texts[index+1].description

# 	if texts[index].description == 'OCENTTE':
# 		idno = texts[index+1].description
# 	# print(i,' ',texts[index].description)
# 	# i += 1

# # print(passno)
# # print(idno)

# file_name = 'C:\Sage\X3PEOPLE\\folders\SEED\PIC\ocrfile.txt' 

# print('Writing to file: ' + file_name)

# file = open(file_name,'w')

# file.write(passno + ';')
# file.write(idno)

# file.close()