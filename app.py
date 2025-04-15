import streamlit as st
import easyocr
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tempfile
import os
from PIL import Image

# Set page title and description
st.set_page_config(page_title="EasyOCR Text Detection", layout="wide")
st.title("Text Detection with EasyOCR")
st.write("Upload an image containing text and the app will detect and extract the text.")

# Initialize EasyOCR reader
@st.cache_resource
def load_model():
    return easyocr.Reader(['en'])

# Function to process image and detect text
def process_image(image_path, reader):
    # Read the image
    img = cv2.imread(image_path)
    
    # Perform OCR
    result = reader.readtext(image_path)
    
    # Create a copy of the image for drawing
    img_with_boxes = img.copy()
    
    # Draw bounding boxes and text on the image
    for detection in result:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        confidence = detection[2]
        
        # Draw rectangle
        cv2.rectangle(img_with_boxes, top_left, bottom_right, (0, 255, 0), 3)
        
        # Add text above the box
        cv2.putText(img_with_boxes, f"{text} ({confidence:.2f})", 
                   (top_left[0], top_left[1] - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Convert BGR to RGB for displaying with Streamlit
    img_with_boxes_rgb = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)
    
    return img_with_boxes_rgb, result

# Main app
reader = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Create a temporary file to save the uploaded image
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_filename = temp_file.name
    temp_file.write(uploaded_file.getvalue())
    temp_file.close()
    
    # Display original image
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
    
    # Process image and display results
    with col2:
        st.subheader("Detected Text")
        
        with st.spinner("Detecting text..."):
            img_with_boxes, result = process_image(temp_filename, reader)
        
        st.image(img_with_boxes, use_column_width=True)
    
    # Show detected text in a table
    st.subheader("Extracted Text")
    
    if len(result) > 0:
        text_data = []
        for idx, detection in enumerate(result):
            text = detection[1]
            confidence = detection[2]
            text_data.append({"No.": idx+1, "Text": text, "Confidence": f"{confidence:.2f}"})
        
        st.table(text_data)
    else:
        st.write("No text detected in the image.")
    
    # Clean up the temporary file
    os.unlink(temp_filename)
else:
    # Display sample info when no image is uploaded
    st.info("Please upload an image to get started.")
    st.write("This app can detect text in various images like signs, documents, and screenshots.")