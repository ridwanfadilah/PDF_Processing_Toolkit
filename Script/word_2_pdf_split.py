import os
from docx import Document
from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter
#----------------------------------------------------
def split_word_to_pdf(docx_path):
    docx_path = docx_path.replace("\\", "/")
    doc = Document(docx_path)
    base_filename = os.path.splitext(os.path.basename(docx_path))[0]
    output_dir = os.path.join(os.path.dirname(docx_path), base_filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    temp_pdf_path = os.path.join(output_dir, f"{base_filename}_temp.pdf")
    convert(docx_path, temp_pdf_path)
    reader = PdfReader(temp_pdf_path)
    
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])    
        output_pdf_path = os.path.join(output_dir, f"{base_filename}_page_{i+1}.pdf")
        with open(output_pdf_path, "wb") as output_pdf_file:
            writer.write(output_pdf_file)
    
    os.remove(temp_pdf_path)
    print(f"Dokumen telah diekspor dan dibagi ke dalam folder: {output_dir}")
#----------------------------------------------------
docx_path = r"D:\MAC\.....docx"
split_word_to_pdf(docx_path)
