import PIL 
from PIL import Image #image module to manipulate image
import pytesseract #api that helps us to convert the image to strings

#below is the location of tesseract that is installed on the system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#image that is to be converted
image = Image.open('1.jpeg');

#simple method that uses an image to convert the image to string
temp = pytesseract.image_to_string(image, lang="eng")

#printing the data
print(temp)
