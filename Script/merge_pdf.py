'''
Menggabungkan dua file PDF dengan meng-copy path filenya
'''
from PyPDF2 import PdfReader, PdfWriter
import os
import shutil
import platform
#----------------------------------------------------
def merge_pdfs(input_paths, output_path):
    pdf_writer = PdfWriter()
    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def get_default_download_directory():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        raise OSError("ERROR")
#----------------------------------------------------
pdf1_path = input("Path file PDF 1: ").strip('"')
pdf2_path = input("path file PDF 2: ").strip('"')
pdf1_path = os.path.normpath(pdf1_path)
pdf2_path = os.path.normpath(pdf2_path)
merged_pdf_name = input("Nama file PDF hasil merge: ")
merged_pdf_path = os.path.join(get_default_download_directory(), merged_pdf_name + ".pdf")
merge_pdfs([pdf1_path, pdf2_path], merged_pdf_path)
print(f"File PDF tersimpan di: {merged_pdf_path}")
print('DONE')
