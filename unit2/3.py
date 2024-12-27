# Splitting PDFs:
from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader("rittoppers.pdf")
writer = PdfWriter()
# Save the first page to a new PDF
writer.add_page(reader.pages[1])
with open("onlyrittoppers.pdf", "wb") as output:
    writer.write(output)
