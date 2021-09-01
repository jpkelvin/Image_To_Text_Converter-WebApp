from PIL import Image
import pytesseract as tess
import os,re,send2trash
tess.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

text=[]
iamge=Image
# path = os.path.dirname(os.path.realpath(__file__))
# input_path = path + '/sampleimages/'
# #opening files and extracting text
# for root,dirs,filenames in os.walk(input_path):
#     for filename in filenames:
try:
    img = Image.open(Image)
    text.append(tess.image_to_string(img))
    send2trash.send2trash(Image)
except:
    print("FInvalid File")
text = str('\n'.join(text))
print(text)