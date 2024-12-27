# Extract Matching Text from pdf using PyPDF2

import re
from PyPDF2 import PdfReader

# Load the PDF
reader = PdfReader("test4.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

# Normalize text to handle line breaks and spaces
text = text.replace("\n", " ").replace("\r", " ")

# Extract invoice number using regex
match = re.search(r"Invoice Number:\s*([\w-]+)", text)
if match:
    print("Invoice Number:", match.group(1))
else:
    print("Invoice Number not found!")

