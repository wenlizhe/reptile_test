import re
import os
import datetime
import random
# import urllib.error
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve


pages = set()
allextlinks = set()
allintlinks = set()
random.seed(datetime.datetime.now())
download_diretory = 'download'
baseurl = 'http://pythonscraping.com'


# 获取页面所有内链的列表
def get_internal_links(bsobj, includeurl):
    interlinks = []
    # 找出所有以"/"开头的链接
    for link in bsobj.findAll('a', href=re.compile('^(/|.*'+includeurl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in interlinks:
                interlinks.append(link.attrs['href'])
    return interlinks


# 获取页面所有外链的列表
def get_external_links(bsobj, excludeurl):
    external_links = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    print(type(bsobj))
    for link in bsobj.findAll('a', href=re.compile("^(http|www)((?!"+excludeurl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])
    return external_links


# 收集网站上发现的所有外链列表
def get_alll_external_links(siteurl):
    html = urlopen(siteurl)
    bsobj = BeautifulSoup(html)
    internal_links = get_internal_links(bsobj, split_address(siteurl)[0])
    external_links = get_external_links(bsobj, split_address(siteurl)[0])
    for link in external_links:
        if link not in allextlinks:
            allextlinks.add(link)
            print(link)
    for link in internal_links:
        if link not in allextlinks:
            print("即将获取链接的URL是:"+link)
            allextlinks.add(link)
            get_alll_external_links(link)


def split_address(adress):
    address_parts = adress.replace('http://', '').split('/')
    return address_parts


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bsobj = BeautifulSoup(html, 'html.parser')
    external_links = get_external_links(bsobj, split_address(starting_page)[0])
    if len(external_links) == 0:
        internal_links = get_internal_links(starting_page, '')
        return get_external_links(internal_links[random.randint(0, len(internal_links)-1)], '')
    else:
        return external_links[random.randint(0, len(external_links)-1)]


def follow_external_only(startingsite):
    external_link = get_random_external_link(startingsite)
    print("随机外链是:"+external_link)
    follow_external_only(external_link)


def test():
    html = urlopen(baseurl)
    bsobj = BeautifulSoup(html, 'html.parser')
    imagelocation = bsobj.find('a', {'id': 'logo'}).find('img')['src']
    urlretrieve(imagelocation, './static/logo.jpg')


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    # follow_external_only('http://oreilly.com')
    # getlinks("")
    test()
    # print(title)
