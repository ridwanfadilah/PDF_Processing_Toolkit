import PyPDF2
import os
#----------------------------------------------------
def split_pdf(input_pdf):
    input_pdf = input_pdf.replace('/', os.sep).replace('\\', os.sep)
    input_pdf = input_pdf.strip('"')
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)

            for page_num in range(total_pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[page_num])
                output_pdf = os.path.join(downloads_folder, f'page_{page_num + 1}.pdf')
                with open(output_pdf, 'wb') as output_file:
                    writer.write(output_file)

                print(f'Halaman {page_num + 1} berhasil disimpan sebagai {output_pdf}')
    except FileNotFoundError:
        print(f"File {input_pdf} tidak ditemukan. Pastikan path file sudah benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
#----------------------------------------------------
input_pdf = input("Masukkan path file PDF: ") # Masukkan path file PDF Anda
split_pdf(input_pdf)
