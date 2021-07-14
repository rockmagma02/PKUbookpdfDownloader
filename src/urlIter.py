import requests
from bs4 import BeautifulSoup
from urllib import parse

class UrlIter:
    def __init__(self, url) -> None:
        self.url = url
        self.request = self.__getRequest()
        self.bs = BeautifulSoup(self.request.text, features='lxml')
        self.title = self.__getTitle()
        self.maxPages = self.__getMaxPages()

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

    def getIter(self, width, height = None):
        PARAM_DICT = {
            'objID': '__need',
            'metaId': '__need',
            'OrgId': '__need',
            'Ip': 'undefined',
            'scale': '',
            'width': width,
            'height': height,
            'pageid': 0,
            'ServiceType': 'Imagepage',
            'scaleType': 1,
            'OrWidth': '__need',
            'OrHeight': '__need',
            'testres': '__need',
            'debug': '__need',
            'SessionId': '__need',
            'UserName': '__need',
            'cult': '__need'
        }
        HTML_p = [
            'txtFileID',
            'txtMetaId',
            'txtOrgIdentifier',
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            'pagesWidth',
            'pagesHeight',
            'txtTestRes',
            'txtDebug',
            'sessionid',
            'txtuserName',
            'txtCultureName'
        ]
        HTML_OTHER_P = 'urlrights'

        paramCount = 0
        for param, sign in PARAM_DICT.items():
            if sign == '__need':
                try:
                    PARAM_DICT[param] = self.bs.find(id=HTML_p[paramCount])['value']
                except:
                    PARAM_DICT[param] = ''
            else:
                PARAM_DICT[param] = str(sign)
            paramCount += 1
        urlRight = self.bs.find(id=HTML_OTHER_P)['value']

        PAGE_PATH= r'OnLineReader/command/imagepage.ashx'
        meta = parse.urlsplit(self.url)
        scheme, netloc = meta.scheme, meta.netloc
        imgUrlPre = parse.ParseResult(scheme, netloc, PAGE_PATH, '', '', '').geturl() + '?'

        PARAM_DICT['scale'] = width / float(PARAM_DICT['OrWidth'])
        PARAM_DICT['width'] = str(PARAM_DICT['scale'] * float(PARAM_DICT['OrWidth']))
        PARAM_DICT['height'] = str(PARAM_DICT['scale'] * float(PARAM_DICT['OrHeight']))
        PARAM_DICT['scale'] = str(PARAM_DICT['scale'])

        def __urlIterGengerate():
            for page in range(1, self.maxPages+1):
                PARAM_DICT['pageid'] = str(page)
                imgUrl = imgUrlPre + parse.urlencode(PARAM_DICT)
                imgUrl += '&'
                imgUrl += urlRight
                yield page, imgUrl
        return __urlIterGengerate()
        

def test():
    urlIter = UrlIter(input())
    urlIter.getIter(1800)

if __name__ == '__main__':
    test()
