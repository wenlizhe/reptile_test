import urllib.request
import urllib.parse
import http.cookiejar
import requests
import urllib.error


def urlliblibray():
    username = 'administrator'
    password = 'administrstor'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/60.0.3112.113 Safari/537.36'
    url = 'http://123.207.71.29/login'
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)"
    values = {'username': username, 'password': password}
    headers = {'User-Agent': user_agent,
               }

    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    get_url = url + '?'+str(data, encoding='utf-8')
    print(get_url)
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    print(str(response.read(), encoding='utf-8'))


def cookielib():
    # 声明Cookiejar对象
    cookie = http.cookiejar.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    # 创建一个请求，原理同urllib2的urlopen
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name = '+item.name)
        print('Value = '+item.value)


def save_cookie():
    filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    postdata = {
        'username': 'administrator',
        'password': 'administrator',
    }
    login_url = 'http://123.207.71.29/login'
    result = opener.open(login_url, postdata)
    cookie.save(ignore_discard=True, ignore_expires=True)
    print(result.read())


def test():
    data = {}
    data['word'] = 'Jecvay Notes'
    url_values = urllib.parse.urlencode(data)
    url = "http://www.baidu.com/s?"
    full_url = url + url_values
    print(full_url)
    data = urllib.request.urlopen(full_url).read()
    data = data.decode('UTF-8')
    print(data)


if __name__ == '__main__':
    # urlliblibray()
    test()
    # save_cookie

