from PIL import Image
import pytesseract

im = Image.open("IMG_9156.JPG")

text = pytesseract.image_to_string(im, lang = 'eng')

file = open("ocr.txt", "w")
file.write(text) 
file.close() 
print(text)
