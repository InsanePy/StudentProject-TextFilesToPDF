from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("textfiles/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    filename = Path(filepath).stem
    name = filename.capitalize()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=0, h=15, txt=f"{name}", ln=1)

pdf.output("output.pdf")