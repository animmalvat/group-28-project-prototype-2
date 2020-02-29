import PIL
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
temp = pytesseract.image_to_string(Image.open('1.jpeg'), lang="eng")
print(temp)
