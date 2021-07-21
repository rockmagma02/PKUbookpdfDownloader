from io import BytesIO
from PIL import Image
from tqdm import tqdm
import requests
import os
def imgDownloaderSingle(imgUrl, page, title = 'unknow', timeout = 60, targetPath = './img/', imgs = []):
    os.makedirs(targetPath, exist_ok=True)
    r = requests.get(imgUrl, timeout = timeout)
    img = Image.open(BytesIO(r.content))
    imgFile = targetPath+title+'{:03d}'.format(page)+'.png'
    img.save(imgFile, 'PNG')
    imgs.append(imgFile)
    return imgs

def imgDownloaderTotal(urlIter, quality = 'high'):
    qualityDict = {'high': 1800, 'middle': 1500, 'low': 900}
    if quality not in qualityDict.keys():
        raise Exception('please give a right quality')
    print('downloade begin')
    imgs = []
    with tqdm(total = urlIter.maxPages) as pagesCounter:
        for page, imgUrl in urlIter.getIter(qualityDict[quality]):
            imgs = imgDownloaderSingle(imgUrl, page, urlIter.title, imgs=imgs)
            pagesCounter.update(1)
    return imgs
