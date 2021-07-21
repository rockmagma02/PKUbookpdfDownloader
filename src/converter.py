from PIL import Image
from fpdf import FPDF
import os

def converter(imgs, PDFPath = './PDF/', title = 'unknow'):
    print('generating a pdf......')
    os.makedirs(PDFPath, exist_ok=True)
    bookPath = PDFPath + title +'.pdf'
    cover = Image.open(imgs[0])
    width, height = cover.size
    pdf = FPDF(unit = 'pt', format = [width, height])
    for page in imgs:
        pdf.add_page()
        pdf.image(page, 0, 0)
    pdf.output(bookPath, 'F')
