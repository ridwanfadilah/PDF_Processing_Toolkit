'''
File excel berisikan beberapa path file PDF yang akan di-merge.
Format excel:
    Nama kolom 1 = PDF 1
    Nama kolom 2 = PDF 2
    Nama kolom 3 = NAMA  FILE

|     PDF 1     |     PDF 2     |     NAMA FILE     |
-----------------------------------------------------
|/path/file/A1  |/path/file/A2  |    Nama_File_A    |
|/path/file/B1  |/path/file/B2  |    Nama_File_B    |
'''

import pandas as pd
import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
#----------------------------------------------------
def merge_pdfs(input_paths, output_path):
    pdf_writer = PdfWriter()
    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def remove_duplicate_pages(input_path, output_path):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()
    previous_page = None
    for page in pdf_reader.pages:
        if page != previous_page:
            pdf_writer.add_page(page)
            previous_page = page
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)
#----------------------------------------------------
Excel = input("Masukkan path file excel: ")
print('Masukkan path folder untuk menyimpan file hasil merge. Jika tidak diisi, maka otomatis tersimpan di Downloads')
Folder = input("Masukkan path folder hasil merge (optinal): ")
if not Folder:
    Folder = str(Path.home() / "Downloads")
Excel = os.path.normpath(Excel.strip('"'))
Folder = os.path.normpath(Folder.strip('"'))
excel_file_path = Excel
df = pd.read_excel(excel_file_path)
for index, row in df.iterrows():
    pdf_paths = [row['PDF 1'], row['PDF 2']]
    output_filename = row['NAMA FILE']
    merged_pdf_path = 'temp_merged_file.pdf'
    merge_pdfs(pdf_paths, merged_pdf_path)
    final_pdf_path = os.path.join(Folder, output_filename + '.pdf')
    remove_duplicate_pages(merged_pdf_path, final_pdf_path)
    os.remove(merged_pdf_path)
print('DONE')
