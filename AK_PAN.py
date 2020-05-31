# from PIL import Image, ImageEnhance
import pytesseract
import re
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def pan_data(x):
    try:
        img = cv.imread(x,0)
        image_pixels=img.shape[0]*img.shape[1]
#         print(image_pixels)
        if image_pixels<250000:
            clahe = cv.createCLAHE(clipLimit=1000, tileGridSize=(img.shape[0],img.shape[1]))
            cl1 = clahe.apply(img)
            cl1=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                        cv.THRESH_BINARY,99,39)
            text=pytesseract.image_to_string(cl1,lang='eng')
            def find_pan(extracted_text):
                if re.search(r"[a-zA-Z]{3}?[abcfghjlptABCFGHJLPT]?[a-zA-z][0-9]{4}[a-zA-Z]", text):
                    return re.search(r"[a-zA-Z]{3}?[abcfghjlptABCFGHJLPT]?[a-zA-z][0-9]{4}[a-zA-Z]", extracted_text).group(0)
                else:
                    return extracted_text[extracted_text.index('Number'):].splitlines()[2].replace(' ', '')
            pan_no=find_pan(text)
            print(text)
            return pan_no
        else:
            # create a CLAHE object (Arguments are optional).
            clahe = cv.createCLAHE(clipLimit=1000, tileGridSize=(img.shape[0],img.shape[1]))
            cl1 = clahe.apply(img)
            cl1=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                        cv.THRESH_BINARY,99,59)
            text=pytesseract.image_to_string(cl1,lang='eng')
            def find_pan(extracted_text):
                if re.search(r"[a-zA-Z]{3}?[abcfghjlptABCFGHJLPT]?[a-zA-z][0-9]{4}[a-zA-Z]", text):
                    return re.search(r"[a-zA-Z]{3}?[abcfghjlptABCFGHJLPT]?[a-zA-z][0-9]{4}[a-zA-Z]", extracted_text).group(0)
                else:
                    return extracted_text[extracted_text.index('Number'):].splitlines()[2].replace(' ', '')
            pan_no=find_pan(text)
            print(text)
            return pan_no
    except:
        print(text)
        return False


pan_data(r"C:\Users\yusharma\Documents\Abbyy DTT Internal Partner\Import\PAN\Capture_1.PNG")