import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader

def count_pages_in_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            return len(pdf.pages)
    except Exception as e:
        print(f'Błąd odczytu pliku PDF: {e} (plik: {file_path})')
        return 0

def count_pages_in_directory(directory_path):
    total_pages = 0
    for root_dir, _, file_names in os.walk(directory_path):
        for file_name in file_names:
            file_path = os.path.join(root_dir, file_name)
            if file_path.endswith('.pdf'):
                total_pages += count_pages_in_pdf(file_path)
    return total_pages

# Utworzenie okna dialogowego do wyboru folderu
root = Tk()
root.withdraw()
directory_path = filedialog.askdirectory(title="Wybierz folder z dokumentami")

if directory_path:
    total_pages = count_pages_in_directory(directory_path)
    print(f'Całkowita ilość stron: {total_pages}')
else:
    print('Nie wybrano folderu.')
