import PyPDF2
import cv2 as cv
from functions import grayscale
import pytesseract


FILE_PATH = './pdf/SLT eBill.pdf'
print(type(FILE_PATH))

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(f)
    #print(page.extractText())




bill = cv.imread('./images/bill_1.jpeg')

# Binarization
gray_image = grayscale(bill)

ocr_result = pytesseract.image_to_string(gray_image)


