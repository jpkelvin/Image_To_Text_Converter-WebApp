from PIL import Image
import pytesseract as tess
import os,re,send2trash
tess.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

path = os.path.dirname(os.path.realpath(__file__))
input_path = path + '/static/images/'
#opening files and extracting text


def extract(img):
    text=[]
    for root,dirs,filenames in os.walk(input_path):
        try:
            img1 = Image.open(input_path + img)
            text.append(tess.image_to_string(img1))
            send2trash.send2trash(input_path+img)
        except:
            # return 'Invalid Image'
            continue
    text = str('\n'.join(text))
    return text