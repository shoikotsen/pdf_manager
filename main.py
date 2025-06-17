print("🚀 Script started")

import os
from PyPDF2 import PdfMerger   # <- library we’ll install in a moment

def merge_pdfs(pdf_list, output_filename="merged_output.pdf"):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    folder = "sample_pdfs"
pdfs = [f"{folder}/{f}" for f in os.listdir(folder) if f.endswith(".pdf")]

print("🧪 Checking files found in sample_pdfs...")
print("PDFs found:", pdfs)

if not pdfs:
    print("❌ No PDF files found in", folder)
else:
    merge_pdfs(pdfs)
    print("✅ Merged", len(pdfs), "files → merged_output.pdf")

