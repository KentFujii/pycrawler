import urllib.request as req
import gzip
from os import path, mkdir

savepath = path.dirname(__file__) + '/mnist'
baseurl = 'http://yann.lecun.com/exdb/mnist'
files = [
    'train-images-idx3-ubyte.gz',
    'train-labels-idx1-ubyte.gz',
    't10k-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz'
]
if not path.exists(savepath):
    mkdir(savepath)

for f in files:
    url = baseurl + '/' + f
    loc = savepath + '/' + f
    print('download:', url)
    if not path.exists(loc):
        req.urlretrieve(url, loc)

for f in files:
    gz_file = savepath + '/' + f
    raw_file = savepath + '/' + f.replace(".gz", '')
    print('gzip:', f)
    with gzip.open(gz_file, 'rb') as fp:
        body = fp.read()
        with open(raw_file, 'wb') as w:
            w.write(body)
print('OK')
