import urllib.request
import urllib.parse
import http.cookiejar
import re
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
    grade_url = 'http://123.207.71.29/results'
    result = opener.open(grade_url)
    print(result.read())


def test():
    url = "http://www.xxxxx.com/"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)"
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url)
    try:
        urllib.request.urlopen(req)
        # content = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
    except urllib.error.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    # urlliblibray()
    test()
    # save_cookie

