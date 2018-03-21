import os
import re
import socket
import collections
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver


url1 = 'http://www.pythonscraping.com/pages/page3.html'


class Downpage(object):
    
    def __init__(self, u):
        self.url = u

    def save_html(self):
        """前往指定页面,下载网页内容"""
        page = requests.get(self.url)
        f = open('mt.html', 'wb')
        f.write(page.content)
        f.close()

    @staticmethod
    def get_mes():
        """读取本地文件，获取内容"""
        htmlfile = open('mt.html', 'r', encoding='utf-8')
        htmlpage = htmlfile.read()
        soup = BeautifulSoup(htmlpage, 'html.parser')
        # 获取所有链接文字内容
        replacedstr = re.sub('<\w>|</\w>|\,|\.|\"|<a\shref=|\(|\)|\/|=|\-|>|\_', '', str(soup.p))
        # 分割字符串
        list1 = replacedstr.split()
        # 计算出现频率
        m = collections.Counter(list1)
        return dict(m)

    def wirte_file(self):
        """将文件中的单词按出现频率进行排列.写入到mt_word.txt"""
        i = 0
        t = []
        d = self.get_mes()
        item = [[v[1], v[0]] for v in d.items()]
        item.sort()
        item = item[::-1]
        while i < len(item):
            t.append(item[i][1])
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


def down_pic():
    """进入网页下载图片"""
    html = urlopen(url1)
    bsobj = BeautifulSoup(html, 'html.parser')
    images = bsobj.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
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


# 递归去除list
def test3(alist):
    tmp = []
    for one in alist:
        if isinstance(one, list):
            tmp.extend(test3(one))
        else:
            tmp.append(one)
    return tmp


def test4(x, lists):
    for o in range(x):
        lists.append(o)
    print(lists)


# 递归:一次走一阶或俩阶楼梯
def test5(m):
    a = {1: 1, 2: 2}
    if m <= 0:
        raise AssertionError('WrongNumber')
    elif m in a.keys():
        return a[m]
    else:
        return test5(m-1) + test5(m-2)


def judge_mail(mail):
    """
    验证邮箱格式
    """
    if len(mail) > 5:
        print(re.match('[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]', mail))
    else:
        print('too short')


def test7(url):
    """
    获得一个URL地址的扩展名
    """
    a = ['.html', '.php', '.asp', '.jsp']
    for lis in a:
        print(re.findall(lis, url))


def test8():
    host = '127.0.0.1'
    port = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()

    print('Connected By:', addr)
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print('recv:', data)
        conn.send(data)
    conn.close()


if __name__ == '__main__':
    # url = 'https://en.wikipedia.org/wiki/Machine_translation'
    # t = Test0(url)
    # t.wirte_file()
    # print(test5(0))
    # test7('http://www.cnblogs.com/fnng/archive/2013/05/20/3089816.html ')
    test8()
