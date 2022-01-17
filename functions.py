import PyPDF2
import numpy as np
import pytesseract
from PIL import Image


def imgToText(image):
    im = Image.open(image)
    ocr_result = pytesseract.image_to_string(im)
    return ocr_result


def pdfToText(pdf):
    reader = PyPDF2.PdfFileReader(pdf)
    page = reader.getPage(0)
    ocr_result = page.extractText()
    return ocr_result
