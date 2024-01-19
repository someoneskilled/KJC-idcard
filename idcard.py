import cv2
import pytesseract
from PIL import Image

# Load Tesseract OCR library (Specify the path to Tesseract executable)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the camera (assuming the camera is the default camera with index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale frame to a PIL Image
    image = Image.fromarray(gray)

    # Use Tesseract OCR to extract text from the image
    text = pytesseract.image_to_string(image)

    # Split the extracted text into lines
    lines = text.split('\n')

    # Iterate through each line of text
    for line in lines:
        # Check if the length of the stripped line is 8 characters,
        # starts with the integer '2', and ends with two integers
        if len(line.strip()) == 8 and line.strip().startswith('2') and line.strip()[-2:].isdigit():
            # Define a rectangle's position and size around the recognized text
            (x, y, w, h) = (10, 50, 300, 50)  # You can adjust these values based on your needs

            # Display the recognized text inside the rectangle on the frame
            cv2.putText(frame, line, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the resulting frame with recognized text and rectangles
    cv2.imshow('ID card text', frame)

    # Check for user input to exit the loop (press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
