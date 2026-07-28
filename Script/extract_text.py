from PyPDF2 import PdfReader
import os
from pathlib import Path
import platform
#----------------------------------------------------
def get_default_download_directory():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        raise OSError("Unsupported operating system")

def extract_text_from_pdf(input_path, output_path):
    pdf_reader = PdfReader(input_path)
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for page in pdf_reader.pages:
            text = page.extract_text()
            out_file.write(text + "\n")
    print(f"Teks diekstraksi ke: {output_path}")
#----------------------------------------------------
input_path = input("Path file PDF yang ingin di-ekstrak teksnya: ").strip('"')
input_path = os.path.normpath(input_path)
output_dir = get_default_download_directory()
output_filename = os.path.splitext(os.path.basename(input_path))[0] + "_extracted_text.txt"
output_path = os.path.join(output_dir, output_filename)
extract_text_from_pdf(input_path, output_path)
print('DONE')
