from PIL import Image
import os

def converter(imgs, PDFPath = './PDF/', title = 'unknow'):
    os.makedirs(PDFPath, exist_ok=True)
    bookPath = PDFPath + title +'.pdf'
    if len(imgs) == 1:
        imgs[0].save(bookPath, 'PDF')
    elif len(imgs) >= 1:
        imgs[0].save(bookPath, 'PDF', save_all = True, quality=100, append_images = imgs[1:])
