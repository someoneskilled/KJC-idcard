# OCR ID Card Text Recognition

This simple Python script uses OpenCV and Tesseract OCR to recognize text from a live camera feed. It is specifically designed to identify and display lines of text matching a certain pattern, useful for extracting information from ID cards.

![Screenshot 2024-01-08 103324](https://github.com/someoneskilled/KJC-idcard/assets/134536864/95740e88-bc56-4950-8bd7-7d39bafb06cf)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required dependencies using the following commands:
   ```
   pip install opencv-python
   pip install pytesseract
   pip install Pillow
   ```

3. Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).

4. Set the Tesseract executable path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

## Usage

1. Run the script using the command:
   ```
   python idcard.py
   ```

2. The script captures the default camera feed and extracts text matching a specified pattern.

3. Press 'q' to exit the application.

Feel free to adjust parameters in the script, such as rectangle position and size, based on your specific requirements.

## Acknowledgments

- This script utilizes OpenCV for image processing and Tesseract OCR for text extraction.
