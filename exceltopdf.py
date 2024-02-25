import pandas
from fpdf import FPDF

pd = pandas.read_excel("./data.xlsx")

for index, row in pd.iterrows():
    pdf = FPDF(orientation="portrait", unit="pt", format="a4")
    pdf.add_page()
    pdf.set_font(family="Times", size=32)
    name = row['name']
    pdf.cell(w=0, h=64, align='C', txt=f"{name}", ln=1)

    pdf.set_font(family="Times", size=24)
    pdf.cell(w=0, h=36, align="C", txt="Description", ln=1)

    for k in row.keys():
        if k == 'name': continue
        pdf.set_font(family="Arial", style="B", size=16)
        entry_name = k
        data = str(row[k])
        pdf.cell(w=100, h=20, txt=f"{entry_name.capitalize()}: ")

        pdf.set_font(family="Arial", size=16)
        pdf.cell(w=0, h=20, txt=f"{data.capitalize()}", ln=1)

    pdf.output(f"{name}.pdf")


