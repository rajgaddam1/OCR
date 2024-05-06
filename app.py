import streamlit as st
import os
import spacy
import cv2
import os,argparse
import pytesseract
from PIL import Image
from io import StringIO
import warnings
warnings.filterwarnings("ignore")
st.header("OCR Model Extract text from images", anchor=None)

# Set the path to Tesseract executable
#pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def text_extraction_from_image(image_uploaded):
    img = Image.open(image_uploaded)
    extract_text = pytesseract.image_to_string(img)
    return extract_text

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
col1, col2 = st.columns([1,2])
with col1:
    if st.button("Extract Text"):
        if uploaded_file is not None:
            extract_text = text_extraction_from_image(uploaded_file)
            st.header("Extracted Text:")
            st.write(extract_text)
with col2:
    if st.button("Display Image"):
        st.image(uploaded_file, caption='Uploaded Image')

        
  
    
