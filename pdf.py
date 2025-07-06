import tkinter as tk 
from tkinter import filedialog 
from pikepdf import Pdf 
import os

def merge_pdfs():
    root = tk.Tk() 
    root.withdraw()  # Hide the main window

file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])

if not file_paths:
    print("No files selected.")
     

new_pdf = Pdf.new()

for file in file_paths:
    old_pdf = Pdf.open(file)
    new_pdf.pages.extend(old_pdf.pages)

save_path = os.path.join(os.path.expanduser("~"), "Documents", "merged.pdf")
new_pdf.save(save_path)
print(f"Merged PDF saved as: {save_path}")

if __name__ == "__main__":
    merge_pdfs() 