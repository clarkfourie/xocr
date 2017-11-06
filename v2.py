import io
from google.cloud import vision

vision_client = vision.Client()
file_name = 'Passport.JPG'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

texts = image.detect_text()
for text in texts:
	print(text.description)