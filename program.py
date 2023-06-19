from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def is_blank_page(image):

    threshold = 200
    image = image.convert("L")  
    histogram = image.histogram()
    num_white_pixels = sum(histogram[threshold:])  
    return num_white_pixels / (image.width * image.height) >= 0.99 

def remove_blank_pages(input_path, output_path):
    input_pdf = PdfReader(input_path)
    output_pdf = PdfWriter()

    pages = convert_from_path(input_path, 200, poppler_path=r'C:\Users\topor\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin')
  
    for i, page in enumerate(pages):
        if not is_blank_page(page):
            output_pdf.add_page(input_pdf.pages[i])  

    with open(output_path, "wb") as output_file:
        output_pdf.write(output_file)

    print("Pomyślnie usunięto puste strony i zapisano nowy plik:", output_path)


root = Tk()
root.withdraw()
input_file_path = askopenfilename(title="Wybierz plik PDF")

if input_file_path:
    output_file_path = asksaveasfilename(title="Zapisz jako", defaultextension=".pdf")

    if output_file_path:
        remove_blank_pages(input_file_path, output_file_path)
    else:
        print("Nie wybrano miejsca zapisu.")
else:
    print("Nie wybrano pliku.")
