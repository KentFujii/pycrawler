from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re
import zipfile

local = '773_ruby_5968.zip'
zf = zipfile.ZipFile(local, 'r')
fp = zf.open('kokoro.txt', 'r')
bindata = fp.read()
text = bindata.decode('shift_jis')

text = re.split(r'\-{5,}', text)[2]
text = re.split(r'底本:', text)[0]
text = text.strip()

t = Tokenizer()
results = []
lines = text.split('\r\n')
for line in lines:
    s = line
    s = s.replace('|', '')
    # ルビを削除
    s = re.sub(r'《.+?》', '', s)
    # 入力注を削除
    s = re.sub(r'［＃.+?］', '', s)
    # 形態素解析
    tokens = t.tokenize(s)
    r = []
    for tok in tokens:
        if tok.base_form == "*":
            w = tok.surface
        else:
            w = tok.base_form
        ps = tok.part_of_speech
        hinsi = ps.split(',')[0]
        if hinsi in ['名詞', '形容詞', '動詞', '記号']:
            r.append(w)
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)

wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')
print('================================================')

model = word2vec.Word2Vec.load('kokoro.model')
print('most similat to 海')
print(model.most_similar(positive=['海']))
