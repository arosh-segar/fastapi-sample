from fastapi import FastAPI, UploadFile, File
from functions import pdfToText, imgToText


app = FastAPI()


@app.get("/")
def index():
    return {"name": "hello"}


@app.post("/image")
def root(file: UploadFile = File(...)):
    return {"text": imgToText(file.file)}


@app.post("/pdf")
def root(file: UploadFile = File(...)):
    return {"text": pdfToText(file.file)}
