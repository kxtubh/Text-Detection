# Text Detection Application using EasyOCR and Streamlit


## Project Overview
This report documents the development of a Text Detection Application using EasyOCR and Streamlit. The application provides a user-friendly web interface for uploading images and extracting text content using Optical Character Recognition (OCR) technology.

## Introduction
In today's digital world, extracting text from images is a valuable capability with applications in document digitization, content accessibility, and automated data entry. This project implements an OCR solution that allows users to upload images containing text and receive both visual and textual output of the detected content.

## Technologies Used
The application leverages several key technologies:

1. **Streamlit**: A Python library for creating web applications with minimal code
2. **EasyOCR**: An open-source OCR engine that supports multiple languages
3. **OpenCV**: Computer vision library used for image processing and visualization
4. **Python**: The core programming language used for development
5. **PIL (Pillow)**: Python Imaging Library for image manipulation
6. **Matplotlib**: Visualization library for displaying images and results
7. **NumPy**: Library for numerical processing of image data

## Application Architecture
The application follows a simple but effective architecture:

1. **User Interface Layer**: Built with Streamlit, providing intuitive controls and result visualization
2. **Processing Layer**: Handles image processing using OpenCV and text detection using EasyOCR
3. **Display Layer**: Presents the results to the user through visualizations and formatted tables

## Key Features

### 1. Text Detection and Recognition
- Utilizes EasyOCR's deep learning models to detect and recognize text in uploaded images
- Supports English language text detection (expandable to multiple languages)
- Provides confidence scores for each detected text element

### 2. Visual Feedback
- Displays the original uploaded image
- Shows a processed image with bounding boxes around detected text
- Includes the recognized text and confidence scores directly on the image

### 3. Structured Results
- Presents extracted text in a table format
- Includes text content and confidence scores for each detection
- Numbers each detection for easy reference

### 4. User Interface
- Clean, responsive web interface
- Simple upload mechanism for images
- Side-by-side comparison of original and processed images
- Informative messages and loading indicators

## Installation and Deployment
The application can be installed by following these steps:

1. Clone the repository
2. Install dependencies using the provided requirements.txt file:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run app.py
   ```
