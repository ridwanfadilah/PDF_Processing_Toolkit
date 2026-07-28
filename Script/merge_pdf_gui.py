import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, END
from PyPDF2 import PdfReader, PdfWriter
import os
from pathlib import Path
#----------------------------------------------------
def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfWriter()
    for path in file_paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def add_files():
    files = filedialog.askopenfilenames(
        title="Pilih file PDF yang akan digabungkan",
        filetypes=[("PDF Files", "*.pdf")])
    for f in files:
        if f not in pdf_list:
            pdf_list.append(f)
            listbox.insert(END, os.path.basename(f))

def remove_selected():
    selected = listbox.curselection()
    if not selected:
        return
    for index in reversed(selected):
        pdf_list.pop(index)
        listbox.delete(index)

def move_up():
    selected = listbox.curselection()
    if not selected or selected[0] == 0:
        return
    index = selected[0]
    pdf_list[index-1], pdf_list[index] = pdf_list[index], pdf_list[index-1]
    listbox.delete(0, END)
    for f in pdf_list:
        listbox.insert(END, os.path.basename(f))
    listbox.select_set(index-1)

def move_down():
    selected = listbox.curselection()
    if not selected or selected[0] == len(pdf_list)-1:
        return
    index = selected[0]
    pdf_list[index+1], pdf_list[index] = pdf_list[index], pdf_list[index+1]
    listbox.delete(0, END)
    for f in pdf_list:
        listbox.insert(END, os.path.basename(f))
    listbox.select_set(index+1)

def merge_files():
    if not pdf_list:
        messagebox.showwarning("Peringatan", "Belum ada file yang dipilih!")
        return
    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Simpan file hasil gabungan sebagai"
    )
    if not output_path:
        return
    try:
        merge_pdfs(pdf_list, output_path)
        messagebox.showinfo("Berhasil", f"File PDF berhasil digabungkan!\n\nLokasi: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

#----------------------------------------------------
root = tk.Tk()
root.title("🔗 PDF Merger - Drag & Drop")
root.geometry("480x500")
root.resizable(False, False)

pdf_list = []

label = tk.Label(root, text="Gabungkan Beberapa File PDF", font=("Segoe UI", 12, "bold"))
label.pack(pady=10)

frame_list = tk.Frame(root)
frame_list.pack(pady=10, fill="both", expand=True)
listbox = Listbox(frame_list, selectmode=tk.SINGLE, height=15, width=60)
listbox.pack(side="left", fill="both", expand=True, padx=5)
scrollbar = tk.Scrollbar(frame_list, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)
tk.Button(frame_buttons, text="➕ Tambah File", command=add_files, width=14).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="➖ Hapus File", command=remove_selected, width=14).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="⬆️ Naik", command=move_up, width=8).grid(row=1, column=0, pady=3)
tk.Button(frame_buttons, text="⬇️ Turun", command=move_down, width=8).grid(row=1, column=1, pady=3)

tk.Button(root, text="🔗 Gabungkan File PDF", command=merge_files,
          bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"), width=30).pack(pady=15)

root.mainloop()
