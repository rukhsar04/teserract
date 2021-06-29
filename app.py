import streamlit as st
import pytesseract
from PIL import Image       # Python Imaging Library, to open image 
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.set_option('deprecation.showfileUploaderEncoding',False)   # To ignore warnings
st.title ("OCR - Optical Character Recognition")               # To print the title 
st.text("Upload the image")  
uploaded_file = st.sidebar.file_uploader("Choose an image..........", type=["jpg","png","jpeg"])
if uploaded_file is not None: 
  img = Image.open(uploaded_file)       #read the image
  st.image(img,caption='Uploaded Image',use_column_width=True)
  st.write("")
  if st.button('PREDICT'):
    st.write("Result.....")  
    extractedInformation=pytesseract.image_to_string(img)
    st.title(extractedInformation)  
    
