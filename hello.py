import re
import time
import socket
from bs4 import BeautifulSoup
from urllib import request
from functools import wraps
from http import cookiejar


url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'


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
    cookie = cookiejar.MozillaCookieJar(filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
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


def socket_client():
    host = '127.0.0.1'
    port = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send('hello'.encode())
    data = s.recv(1024)
    s.close()
    print('Received:', data)


if __name__ == '__main__':
    # test1()
    socket_client()
