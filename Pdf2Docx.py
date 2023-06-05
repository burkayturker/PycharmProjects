from pdf2docx import Converter

pdf_path = "TanerBurkayTürker.pdf"
docx_path = "TanerBurkayTürker.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()
