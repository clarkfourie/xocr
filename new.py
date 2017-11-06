import io
from google.cloud import vision
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

###############################################################################
# Variable inputs
###############################################################################

file_name = '\ocr.txt' # file name to be written to and read from X3 (keep preceding "\"")
img_pwd = filedialog.askopenfilename(initialdir = 'C:/Sage/X3PEOPLE/folders/SEED/PIC') # select image
file_pwd = 'C:\Sage\X3PEOPLE\\folders\SEED\PIC\\'  + file_name

###############################################################################


client = vision.Client()

print('Loading image...')

with io.open(img_pwd, 'rb') as image_file:
	image = client.image(content=image_file.read())

print('Performing Optical Character Recognition')

labels = image.detect_labels(limit=3)
for label in labels:
	print(label.description) 

index0 = last_name = first_name = given_names = nationality = passno = idno = ''

texts = image.detect_text()
index = 0
index0 = texts[index].description.encode('ascii', 'ignore').decode('ascii')[:4] # slice four chars from left

print('Extracting specific fields')
# print(index0)

###############################################################################
# 1.1) New ZAF passport
###############################################################################

if (index0 == 'Pass'): 
	for index in range(len(texts)):
		if texts[index].description.encode('ascii', 'ignore').decode('ascii')[-3:] == 'Nom': 		# last_name
			last_name = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'pays': 			# Nationality
			nationality = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'passeport': 		# Passno
			passno = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == passno: 			# first_name
			first_name = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'Prnoms': 			# Given names
			mx = index + 1
			while (texts[mx].description.encode('ascii', 'ignore').decode('ascii').lower() != 'nationality'):
				given_names += texts[mx].description.encode('ascii', 'ignore').decode('ascii') + ' '
				mx += 1
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'Sexe': # ID no
			idno = texts[index+1].description

	# # the first name is appended to given name if not already included
	# if first_name in given_names: 
	# 	given_names = given_names[:-1] # slice redundant appended space
	# else:
	# 	given_names += first_name

###############################################################################

###############################################################################
# 1.2) Old ZAF passport
###############################################################################	

if (index0 == 'REPU'): # Old ZAF passport
	for index in range(len(texts)):
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'NOM': 			# last_name
			last_name = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == '-PRENOMS': 		# Given names
			mx = index + 1
			while (texts[mx].description.encode('ascii', 'ignore').decode('ascii').lower() != 'nationality'):
				given_names += texts[mx].description.encode('ascii', 'ignore').decode('ascii') + ' '
				mx += 1
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'NATIONALITE': 	# Nationality
			nationality = texts[index+1].description.encode('ascii', 'ignore').decode('ascii') + ' ' + texts[index+2].description.encode('ascii', 'ignore').decode('ascii') # old passport does not contain the text ZAF, writes out SOUTH AFRICA
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'SUD': 			# Passno
			passno = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')
		if texts[index].description.encode('ascii', 'ignore').decode('ascii') == 'OCENTTE': 		# ID no
			idno = texts[index+1].description.encode('ascii', 'ignore').decode('ascii')

	# Remove the first name and space from given name
	first_name = given_names.split(" ")[0]
	given_names = given_names.replace(first_name + " ",'')

###############################################################################

###############################################################################
# A) Nationality normalisation
###############################################################################

norm_nat = nationality.lower().replace(" ", "")

if norm_nat == 'zaf' or norm_nat == 'southafrica':
	nationality = 'ZA'

###############################################################################

# Console printing

print(last_name)
print(first_name)
print(given_names)
print(nationality)
print(passno)
print(idno)
		
print('Writing to file: ' + file_pwd)

file = open(file_pwd,'w')

file.write(last_name + ';')
file.write(first_name + ';')
file.write(given_names + ';')
file.write(nationality + ';')
file.write(passno + ';')
file.write(idno)

file.close()

# I found elegant work around for me to remove symbols and continue to keep string as string in follows:
# yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')