from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="pt", format="A4")
pdf.add_page()

pdf.image("./meme-example.jpg", w=280, h=184,x=pdf.w/2-140)
pdf.set_font(family="Times", size=24)
pdf.cell(w=0, h=50, txt="That's the meme text", align="C")

pdf.output("./meme.pdf")
