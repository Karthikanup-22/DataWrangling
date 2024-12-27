#Text Extraction using pdfminer

from pdfminer.high_level import extract_text

text = extract_text("test1.pdf")
print(text)
