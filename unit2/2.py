# Merging PDFs

from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("test1.pdf")
merger.append("DW_unit1.pdf")
merger.write("rittoppers.pdf")
merger.close()
