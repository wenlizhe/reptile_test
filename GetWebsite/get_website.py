import re
import os
import time
import datetime
import random
# import urllib.error
from functools import wraps
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve


pages = set()
allextlinks = set()
allintlinks = set()
random.seed(datetime.datetime.now())
download_diretory = 'download'
baseurl = 'http://pythonscraping.com'
wikiurl = 'http://en.wikipedia.org'


# 用来检测函数运行时间
def fn_timer(fn):
    @wraps(fn)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = fn(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" % (fn.__name__, str(t1-t0)))
        return result
    return function_timer


def get_link(pageurl):
    global pages
    html = urlopen(wikiurl+pageurl)
    print()
    bsobj = BeautifulSoup(html, 'lxml')
    for link in bsobj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                get_link(newpage)


if __name__ == '__main__':
    get_link(wikiurl)
