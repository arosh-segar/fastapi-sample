import PyPDF2
import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv.erode(image, kernel, iterations=1)
    image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    image = cv.medianBlur(image, 3)
    return (image)


def imgToText(image):
    im = Image.open(image)
    ocr_result = pytesseract.image_to_string(im)
    return ocr_result


def pdfToText(pdf):
    reader = PyPDF2.PdfFileReader(pdf)
    page = reader.getPage(0)
    ocr_result = page.extractText()
    return ocr_result
