# Author: Shoikot Sen
# Description: This Python script merges all PDF files found in the "sample_pdfs" folder
#              into a single PDF file named "merged_output.pdf" using the PyPDF2 library.

print("🚀 Script started")  # Indicates the script has started running

import os  # Used to interact with the file system (like listing files in a folder)
from PyPDF2 import PdfMerger  # Importing the PdfMerger class from PyPDF2 for combining PDFs

# Function to merge a list of PDF files into one
def merge_pdfs(pdf_list, output_filename="merged_output.pdf"):
    merger = PdfMerger()  # Create a PdfMerger object
    for pdf in pdf_list:
        merger.append(pdf)  # Add each PDF file to the merger
    merger.write(output_filename)  # Write out the merged PDF
    merger.close()  # Close the merger to free up resources

# Run the merging only if this script is executed directly
if __name__ == "__main__":
    folder = "sample_pdfs"  # Folder where the PDF files are located

# Get a list of all PDF files in the specified folder
pdfs = [f"{folder}/{f}" for f in os.listdir(folder) if f.endswith(".pdf")]

print("🧪 Checking files found in sample_pdfs...")
print("PDFs found:", pdfs)  # Print the list of PDFs found

# If no PDFs are found, notify the user. Otherwise, merge them.
if not pdfs:
    print("❌ No PDF files found in", folder)
else:
    merge_pdfs(pdfs)  # Call the function to merge the PDFs
    print("✅ Merged", len(pdfs), "files → merged_output.pdf")  # Success message
