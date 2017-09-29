import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


download_directory = './static/'
baseurl = 'http://pythonscraping.com'


def get_absolute_url(url, source):
    if source.startswith('http://www'):
        u = 'http://'+source[11:]
    elif source.startswith('http://'):
        u = source
    elif source.startswith('www.'):
        u = source[4:]
        u = 'http://'+u
    else:
        u = url+'/'+source
    if url not in u:
        return None
    return u


def get_download_path(url, absolute_url, directory):
    path = absolute_url.replace('www.', '')
    path = path.replace(url, '')
    path = directory+path
    dirc = os.path.dirname(path)

    if not os.path.exists(dirc):
        os.makedirs(dirc)

    return path


def test(url, directory):
    html = urlopen(baseurl)
    bsobj = BeautifulSoup(html, 'html.parser')
    download_list = bsobj.findAll(src=True)

    file_url = ''
    for download in download_list:
        file_url = get_absolute_url(url, download['src'])
        if file_url is not None:
            print(file_url)
        urlretrieve(file_url, get_download_path(url, file_url, directory))


if __name__ == '__main__':
    test(baseurl, download_directory)
