import cv2
import streamlit as st
from PIL import Image
import numpy as np

st.title("Filters Application")


def blackwhite(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_image


def pencil_sketch(img, ksize=5):
    blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    sketch, _ = cv2.pencilSketch(blur)
    return sketch


def HDR(img, level=50, simga_s=10, sigma_r=0.1):
    bright = cv2.convertScaleAbs(img, beta=level)
    hd_image = cv2.detailEnhance(bright, sigma_s=simga_s, sigma_r=sigma_r)
    return hd_image


def Brightness(img, level=50):
    bright = cv2.convertScaleAbs(img, beta=level)
    return bright


def style_image(img, ksize=5, simga_s=10, sigma_r=0.1):
    blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    style = cv2.stylization(blur, sigma_s=simga_s, sigma_r=sigma_r)
    return style


upload = st.file_uploader("Choose an image", type=["png", "jpg"])
if upload is not None:
    img = Image.open(upload)  # read
    img = np.array(img)
    original_image, output_image = st.columns(2)

    with original_image:
        st.header("Original")
        st.image(img, use_column_width=True)
    st.header("FilterS List")
    options = st.selectbox(
        "Select Filters", ("None", "BlackWhite", "style_image", "pencil_sketch", "HDR", "Brightness")
    )

    if options == "None":
        output = img
    elif options == "BlackWhite":
        output = blackwhite(img)
    elif options == "pencil_sketch":
        kvalue = st.slider("Kernel Size", 1, 9, 4, step=2)
        output = pencil_sketch(img, kvalue)
    elif options == "HDR":
        level = st.slider("level", -50, 50, 10, step=10)
        simga_s = st.slider("simga_s", 5, 10, 10, step=1)
        output = HDR(img, level=level, simga_s=simga_s)
    elif options == "Brightness":
        level = st.slider("level", -50, 50, 10, step=10)
        output = Brightness(img, level=level)
    elif options == "style_image":
        kvalue = st.slider("Kernel Size", 1, 9, 3, step=2)
        simga_s = st.slider("simga_s", 5, 10, 10, step=1)
        output = style_image(img, kvalue, simga_s)
    with output_image:
        st.header("Output Image")
        st.image(output)
