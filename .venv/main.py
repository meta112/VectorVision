import pytesseract
from PIL import Image

print("Tesseract prediction for typed digits: ")
print(pytesseract.image_to_string(Image.open('.venv/maxresdefault.jpg')))

print("Tesseract prediction for handwritten digits: ")
print(pytesseract.image_to_string(Image.open('.venv/handwritten_matrix.jpg')))
