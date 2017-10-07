from os import path
from os import mkdir
from urllib import request as req
from urllib.parse import urljoin
from parsel import Selector

url = 'http://keison.sakura.ne.jp'
res = req.urlopen(url)
html = res.read().decode('utf-8')
selector = Selector(text=html)
links = selector.xpath(
    "//ul[@id='index']/li[position() <= 8]/a/@href").extract()
links = [urljoin(url, link) for link in links]
zip_links = []
for link in links:
    res = req.urlopen(link)
    html = res.read().decode('utf-8')
    selector = Selector(text=html)
    target_links = selector.xpath(
        """
            //div[@id='main']/ul/li/a[
                contains(text(), '夏目漱石') or
                contains(text(), '太宰治') or
                contains(text(), '芥川龍之介')]/@href
        """).extract()
    target_links = [urljoin(link, target_link) for target_link in target_links]
    for target_link in target_links:
        zip_links.append(target_link)

local = 'text'
for zip_link in zip_links:
    persons = ['芥川龍之介', '太宰治', '夏目漱石']
    if 'akutagawa' in zip_link:
        person = '芥川龍之介'
    elif 'dazai' in zip_link:
        person = '太宰治'
    else:
        person = '夏目漱石'
    save_dir = local + '/' + person
    if not path.exists(save_dir):
        print('ZIPファイルをダウンロード')
        if not path.exists(local):
            mkdir('text')
        req.urlretrieve(zip_link, save_dir + '.zip')
