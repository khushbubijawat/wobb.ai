import pytesseract
import PyPDF2
from PIL import Image

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def extract_text_from_image(image_path):
    """Extracts text from an image using Tesseract OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_text_from_url(url):
    """Extracts text from a URL (future scope, for web scraping)."""
 
    pass
