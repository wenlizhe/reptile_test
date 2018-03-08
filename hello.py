import re
import time
from bs4 import BeautifulSoup
from urllib import request
from functools import wraps
from http import cookiejar


url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'


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


@fn_timer
def test1():
    html = request.urlopen(url)
    bsobj = BeautifulSoup(html, 'lxml')
    for link in bsobj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def get_cookie():
    filename = 'cookie.txt'
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.MozillaCookieJar(filename)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def use_cookie():
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    # test1()
    use_cookie()
