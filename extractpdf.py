import fitz

pdffile = "./FULLTEXT01.pdf"

with fitz.open(pdffile) as pdf:
    for page in pdf:
        text = page.get_textpage()
        print(text.extractText())

