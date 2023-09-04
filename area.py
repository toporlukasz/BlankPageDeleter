import os
import fitz
from tkinter import Tk, filedialog

def count_pdf_area(folder_path):
    total_area = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            with fitz.open(file_path) as doc:
                for page in doc:
                    mediabox = page.mediabox
                    page_width = mediabox[2] - mediabox[0]
                    page_height = mediabox[3] - mediabox[1]
                    page_area = page_width * page_height
                    total_area += page_area

    return total_area / 1000000  # Przelicz na metry kwadratowe

# Wybór lokalizacji folderu za pomocą okna dialogowego
root = Tk()
root.withdraw()
folder_path = filedialog.askdirectory(title="Wybierz folder z plikami PDF")

if folder_path:
    total_area = count_pdf_area(folder_path)
    print(f"Całkowita powierzchnia PDF-ów w folderze: {total_area} metrów kwadratowych")
else:
    print("Nie wybrano folderu.")
