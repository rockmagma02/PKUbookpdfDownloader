from src.urlIter import UrlIter
from src.downloader import imgDownloaderTotal
from src.converter import converter

def downloader():
    urlIter = UrlIter(input())
    imgs = imgDownloaderTotal(urlIter, quality = 'low')
    converter(imgs, title = urlIter.title)

if __name__ == '__main__':
    downloader()