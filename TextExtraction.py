import pytesseract
from PIL import Image

def ocr_extraction(img_path):
    image = Image.open(img_path)
    text = pytesseract.image_to_string(image)
    return text
