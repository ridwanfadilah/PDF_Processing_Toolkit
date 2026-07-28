import subprocess
import os

GS_PATH = r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe"
# ↑ sesuaikan dengan versi di laptop kamu

def compress_pdf(input_pdf, output_pdf, quality="ebook"):
    gs_command = [
        GS_PATH,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]

    subprocess.run(gs_command, check=True)

compress_pdf(
    input_pdf = r"C:\Users\rowai\Downloads\1.pdf",
    output_pdf = r"C:\Users\rowai\Downloads\2.pdf",
    quality="ebook"
)

print("PDF berhasil dikompres")
