import requests
from bs4 import BeautifulSoup


class UrlIter:
    def __init__(self, url) -> None:
        self.url = url
        self.request = self.__getRequest()
        self.bs = BeautifulSoup(self.request.text, features='lxml')
        self.title = self.__getTitle()
        self.maxPages = self.__getMaxPages()
        # TODO

    def __getRequest(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r
        else:
            raise Exception("connect fail, plaese check out url")

    def __getTitle(self):
        title = self.bs.find('title').text
        titleLen = len(title)
        return title[17:-6]

    def __getMaxPages(self):
        MAXPAGEID = 'TotalCount'
        maxPagesCount = self.bs.find(id=MAXPAGEID).text
        return int(maxPagesCount)

    def getIter(self):
        QUARY_TUPLE = [
            ('objID', 'txtFileID'),
            ('metaId', 'txtMetaId'),
            ('OrgId', 'txtOrgIdentifier'),
            ('Ip', )
        ]
        pass

    # TODO

def test():
    urlIter = UrlIter(input())
    pass


if __name__ == '__main__':
    test()
