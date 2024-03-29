from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = 'img.jpg'
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
            
text = pytesseract.image_to_string(Image.open('img.jpg'))
file = open("ocr.txt", "w") 
file.write(text) 
file.close()
print(text)
