import requests
import json
import os
import xlrd
from requests.auth import HTTPDigestAuth


host = 'http://127.0.0.1:8000/'


def test_get():
    endpoint = 'get'
    url = ''.join([host,endpoint])
    headers = {"User-Agent":"test request headers"}
    params = {'show_env': '1'}
    r = requests.get(url, headers=headers)
    print(type(r))
    print(eval(r.text)['headers']['User-Agent'])
    print(r.url)


def test_post():
    endpoint = 'post'
    url = ''.join([host, endpoint])
    headers = {'USer-Agent': 'test post'}
    params = {'key1': 'params1', 'key2': 'params2'}
    data = {'site':[
        {'name': 'aaa', 'url': 'www.aaa.com'},
        {'name': 'bbb', 'url': 'www.bbb.com'},
        {'name': 'ccc', 'url': 'www.ccc.com'}
    ]}
    r = requests.post(url, json=data, params=params)
    

def test_cookies():
    endpoint = 'cookies'
    url = ''.join([host, endpoint])
    s = requests.session()
    c = requests.cookies.RequestsCookieJar()
    c.set('c-name', 'c-value', path='/xxx/uuu', domain='.test.com')
    s.cookies.update(c)
    print(s)


def test_session():
    endpoint = 'headers'
    url = ''.join([host, endpoint])
    headers1 = {'a': 'aa'}
    headers2 = {'b': 'bb'}
    s = requests.session()
    s.headers.update(headers1)
    r = s.get(url, headers=headers2)

    s.headers['a'] = None
    r1 = s.get(url, headers=headers2)
    print(r1.text)


def test1():
   pass
    

if __name__ == '__main__':
    pass
