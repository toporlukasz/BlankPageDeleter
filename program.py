import time
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def is_blank_page(image):
    threshold = 200
    image = image.convert("L")
    histogram = image.histogram()
    num_white_pixels = sum(histogram[threshold:])
    return num_white_pixels / (image.width * image.height) >= 0.99

def remove_blank_pages(input_paths):
    for input_path in input_paths:
        start_time = time.time()
        input_pdf = PdfReader(input_path)
        output_pdf = PdfWriter()
        num_blank_pages_removed = 0

        pages = convert_from_path(input_path, 200, poppler_path=r'C:\Users\topor\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin')

        for i, page in enumerate(pages):
            if not is_blank_page(page):
                output_pdf.add_page(input_pdf.pages[i])
            else:
                num_blank_pages_removed += 1

        output_path = input_path  # Nadpisanie oryginalnego pliku

        with open(output_path, "wb") as output_file:
            output_pdf.write(output_file)

        elapsed_time = time.time() - start_time
        print("Usunięto", num_blank_pages_removed, "pustych stron z pliku:", output_path)
        print("Czas przetwarzania:", round(elapsed_time, 2), "sekundy")


root = Tk()
root.withdraw()
input_file_paths = askopenfilenames(title="Wybierz pliki PDF")

if input_file_paths:
    remove_blank_pages(input_file_paths)
else:
    print("Nie wybrano żadnych plików.")
