from bs4 import BeautifulSoup
from urllib import request, parse
from os import makedirs, path
import time
import re

proc_files = {}


def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select('link[rel="stylesheet"]')
    links += soup.select('a[href]')
    result = []
    for a in links:
        href = a.attrs['href']
        url = parse.urljoin(base, href)
        result.append(url)
    return result


def download_file(url):
    o = parse.urlparse(url)
    savepath = './' + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = path.dirname(savepath)
    if path.exists(savepath):
        return savepath
    if not path.exists(savedir):
        print('mkdir=', savedir)
        makedirs(savedir)
    try:
        print("download=", url)
        request.urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print('ダウンロード失敗:', url)
        return None


def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return
    proc_files[savepath] = True
    print('analize_html=', url)
    html = open(savepath, 'r', encoding='utf-8').read()
    links = enum_links(html, url)
    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r'.(css$)', link_url):
                continue
        if re.search(r".(html|htm)$", link_url):
            analize_html(link_url, root_url)
            continue
        download_file(link_url)


url = 'http://docs.python.jp/3.5/library/'
analize_html(url, url)
