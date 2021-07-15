from src.urlIter import UrlIter
from src.downloader import imgDownloaderTotal
from src.converter import converter

def downloader():
    print('''在下载前，请确保同意以下条目
您不会以任何形式传播本代码爬取的电子书
您不会使用本工具得到的电子书牟利
您不会以任何形式修改、商用、传播本代码
您不会过多使用本工具，以攻击[北京大学教参平台](http://162.105.138.126/Usp)服务器
一切违反上述条目的行为，您会承担所有责任，并对开发者免责''')
    answer = input('请输入yes以同意上述')
    if answer != 'yes':
        exit(0)
    print('url, please:    ')
    urlIter = UrlIter(input())
    quality = input('您希望下载电子书的清晰程度（可能影响文件体积和下载速度）：high/middle/low\n')
    imgs = imgDownloaderTotal(urlIter, quality = quality)
    converter(imgs, title = urlIter.title)

if __name__ == '__main__':
    try:
        downloader()
    except Exception as e:
        print(e)
        exit(0)