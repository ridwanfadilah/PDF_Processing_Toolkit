from pdf2docx import Converter

pdf_path = r"C:\Users\Downloads\....pdf"
docx_path = r"C:\Users\OneDrive\.....docx"

cv = Converter(pdf_path)
cv.convert(docx_path, start=0, end=None)
cv.close()

print("Konversi selesai!")
