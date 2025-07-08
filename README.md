#Image Filters Web App using Streamlit & OpenCV &pytesseract
This project is a Streamlit web app that allows users to upload an image and apply various filters like black and white, HDR, brightness adjustment, pencil sketch, and stylized effects using OpenCV.

🧰 Features
Upload images (.jpg, .png)

Apply real-time filters with adjustable parameters:

Black & White

Pencil Sketch

HDR Enhancement

Brightness Control

Stylized Image (Cartoon style)

Side-by-side comparison of original and filtered image

📦 Requirements
Install dependencies using pip:

bash
Copy
Edit
pip install streamlit opencv-python pillow numpy
🚀 Run the App
bash
Copy
Edit
streamlit run app.py
(Replace app.py with your actual filename)

💻 Code Overview
python
Copy
Edit
import cv2
import streamlit as st
from PIL import Image
import numpy as np

st.title("Filters Application")

def blackwhite(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def pencil_sketch(img, ksize=5):
    blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    sketch, _ = cv2.pencilSketch(blur)
    return sketch

def HDR(img, level=50, simga_s=10, sigma_r=0.1):
    bright = cv2.convertScaleAbs(img, beta=level)
    return cv2.detailEnhance(bright, sigma_s=simga_s, sigma_r=sigma_r)

def Brightness(img, level=50):
    return cv2.convertScaleAbs(img, beta=level)

def style_image(img, ksize=5, simga_s=10, sigma_r=0.1):
    blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    return cv2.stylization(blur, sigma_s=simga_s, sigma_r=sigma_r)
📷 How It Works
User uploads an image

The original image is displayed

A filter is selected via dropdown menu

User adjusts filter parameters (if applicable)

The output image is shown next to the original

📁 File Structure
bash
Copy
Edit
project-folder/
│
├── app.py                   # Streamlit application
├── requirements.txt         # Optional dependencies file
└── README.md                # This file
