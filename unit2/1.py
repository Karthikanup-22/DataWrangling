# extracting text from pdf
from PyPDF2 import PdfReader

# Load the PDF file
reader = PdfReader("test3.pdf")

# Extract text from all pages
text = ""
for page in reader.pages:
    text += page.extract_text()

print(text)
