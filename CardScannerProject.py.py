import streamlit as st
from PIL import Image
import numpy as np

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
st.title("Document Scanner Application")


def extract_text(img):
    text = pytesseract.image_to_string(img)
    return text

upload = st.file_uploader("Please upload an image",type=["jpg","png","webp"])

if upload is not None:
    img = Image.open(upload)
    image_array = np.array(img)
    st.image(img)
    text = extract_text(image_array)
    text_list =text.splitlines()
    st.write(text_list)
    