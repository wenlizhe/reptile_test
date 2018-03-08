import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class GetBook(object):
    def __init__(self, weburl):
        self.weburl = weburl

    def getbook(self):
        try:
            html = urlopen(self.weburl)
            bsobj = BeautifulSoup(html.read(), 'lxml')
            print(bsobj.body)
        except AttributeError as e:
            print(str(e))


if __name__ == '__main__':
    url = 'https://book.douban.com/'
    a = GetBook(url)
    a.getbook()
