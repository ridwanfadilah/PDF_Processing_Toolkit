import os
import shutil
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
        raise OSError("ERROR")

def duplicate_pdf(input_path, output_dir, num_copies):
    input_path = os.path.normpath(input_path)
    input_filename = os.path.splitext(os.path.basename(input_path))[0]
    input_ext = os.path.splitext(input_path)[1]
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, num_copies + 1):
        output_filename = f"{input_filename}_{i}{input_ext}"
        output_path = os.path.join(output_dir, output_filename)
        shutil.copy(input_path, output_path)
        print(f"File copied to: {output_path}")
#----------------------------------------------------
input_path = input("Path file PDF yang ingin diduplikasi: ").strip('"')
num_copies = int(input("Jumlah duplikasi: "))
output_dir = input("Masukkan path folder untuk menyimpan file hasil duplikasi. Jika tidak diisi, maka otomatis tersimpan di Downloads: ").strip('"')
if not output_dir:
    output_dir = get_default_download_directory()
output_dir = os.path.normpath(output_dir)
duplicate_pdf(input_path, output_dir, num_copies)
print('DONE')
