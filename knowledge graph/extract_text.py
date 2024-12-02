from pdfminer.high_level import extract_text
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup
import requests
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust if necessary


def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None


def extract_text_from_url(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from URL: {e}")
        return None


if __name__ == "__main__":
    
    pdf_text = extract_text_from_pdf("question 73 rpsc.pdf")
    if pdf_text:
        print("PDF Text Extracted Successfully")

   
    image_text = extract_text_from_image("withtext.jpg")
    if image_text:
        print("Image Text Extracted Successfully")

   
    url_text = extract_text_from_url("https://example.com")
    if url_text:
        print("URL Text Extracted Successfully")
