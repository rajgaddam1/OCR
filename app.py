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

def text_extraction_from_image(image_uploaded):
    img = Image.open(image_uploaded)
    extract_text = pytesseract.image_to_string(img)
    return extract_text

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    extract_text = text_extraction_from_image(uploaded_file)
    st.write(extract_text)


        
  
    
