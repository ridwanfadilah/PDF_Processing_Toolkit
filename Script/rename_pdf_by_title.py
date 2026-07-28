import fitz  #PyMuPDF
import os
import re
#----------------------------------------------------
def extract_table_title(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            
            match = re.search(r'REKAP NILAI KOMPETENSI PER .*?\n(.*?)\n', text) #<----------- sesuaikan dengan data
            if match:
                second_line = match.group(1).strip()
                return second_line
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return None

def rename_pdfs_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)
            title = extract_table_title(pdf_path)
            if title:
                safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
                new_filename = f"{safe_title}.pdf"
                new_path = os.path.join(directory_path, new_filename)
                
                counter = 1
                while os.path.exists(new_path):
                    new_filename = f"{safe_title}_{counter}.pdf"
                    new_path = os.path.join(directory_path, new_filename)
                    counter += 1
                
                os.rename(pdf_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"No valid title found in '{filename}'")
#----------------------------------------------------
directory_path = 'C:/Users/MS-14D2/Documents/..../PDFs'
rename_pdfs_in_directory(directory_path)
