from bs4 import BeautifulSoup
import collections
import requests
from urllib.request import urlopen
import re
import os
from selenium import webdriver


url = 'https://en.wikipedia.org/wiki/Machine_translation'
url1 = 'http://www.pythonscraping.com/pages/page3.html'


def save_html():
    page = requests.get(url)
    f = open('mt.html', 'wb', encoding='utf-8')
    f.write(page.content)
    f.close()


def get_mes():
    htmlfile = open('mt.html', 'r', encoding='utf-8')
    htmlpage = htmlfile.read()
    soup = BeautifulSoup(htmlpage, 'html.parser')
    replacedstr = re.sub('<\w>|</\w>|\,|\.|\"|<a\shref=|\(|\)|\/|=|\-|>|\_', '', str(soup.p))
    list1 = replacedstr.split()
    m = collections.Counter(list1)
    return dict(m)


def wirte_file():
    i = 0
    t = []
    d = get_mes()
    l = [[v[1], v[0]] for v in d.items()]
    l.sort()
    l = l[::-1]
    while i < len(l):
        t.append(l[i][1])
        i += 1
    f = open('mt_word.txt', 'w', encoding='utf-8')
    f.write(' '.join(t))
    f.close()


def test1(m):
    n, a, b = 0, 1, 1
    while n < m:
        yield a
        a, b = b, a + b
        n += 1


def test2():
    html = urlopen(url1)
    bsobj = BeautifulSoup(html, 'html.parser')
    images = bsobj.findAll('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
    for image in images:
        print(image['src'])


def print_directory_contents(spath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    for schild in os.listdir(spath):
        schildpath = os.path.join(spath, schild)
        if os.path.isdir(schildpath):
            print_directory_contents(schildpath)
        else:
            print(schildpath)


class test3:
    def __init__(self,day=0, month=0, year=0):
        self.day=day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int,date_as_string.split('-'))
        my_date = cls(day, month, year)
        return my_date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


class Root(object):
    def __init__(self):
        print("this is Root")

    def a(self):
        print('hello')


class B(Root):
    def __init__(self):
        print("enter B")
        # print(self)  # this will print <__main__.D object at 0x...>
        super(B, self).__init__()
        print("leave B")


class C(Root):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


class D(B, C):
    pass


# 递归去除list
def myextend(alist):
    tmp = []
    for one in alist:
        if isinstance(one, list):
            tmp.extend(myextend(one))
        else:
            tmp.append(one)
    return tmp


def test(x, l=[]):
    for o in range(x):
        l.append(o)
    print(l)


if __name__ == '__main__':     
    # my_date = test3.from_string('11-09-2012')
    # print(my_date.day, my_date.month, my_date.year)
    # is_date = test3.is_date_valid('13-13-2012')
    # print(is_date)
    # d = D()
    # print(d.__class__.__mro__)
    # t = [1,2,5,[3,[],5,2,[57]],90]
    # print(t)
    # print(myextend(t)) 
    pass
