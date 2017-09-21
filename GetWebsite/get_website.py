import re
import datetime
import random
# import urllib.error
from bs4 import BeautifulSoup
from urllib.request import urlopen


pages = set()
random.seed(datetime.datetime.now())


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


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    follow_external_only('http://oreilly.com')
    # getlinks("")
    # test(url)
    # print(title)
