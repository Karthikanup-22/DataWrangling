# Extract Matching Text from pdf using PDFMiner

from pdfminer.high_level import extract_text
import re

text = extract_text("test4.pdf")
text = text.replace("\n", " ").replace("\r", " ")

match = re.search(r"Invoice Number:\s*([\w-]+)", text)
if match:
    print("Invoice Number:", match.group(1))
else:
    print("Invoice Number not found!")
