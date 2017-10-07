import re
import zipfile
from janome.tokenizer import Tokenizer


def tokenize(text):
    t = Tokenizer()
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本:', text)[0]
    text = text.strip()
    text = text.replace('|', '')
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    lines = text.split('\r\n')
    results = []
    for line in lines:
        res = []
        tokens = t.tokenize(line)
        for tok in tokens:
            bf = tok.base_form
            if bf == '*':
                bf = tok.surface
            ps = tok.part_of_speech
            hinsi = ps.split(',')[0]
            if hinsi in ['名詞', '動詞', '形容詞', '記号']:
                res.append(bf)
        l = ' '.join(res)
        results.append(l)
    return results


persons = ['夏目漱石', '太宰治', '芥川龍之介']
sakuhin_count = {}
for person in persons:
    person_dir = './text/' + person
    sakuhin_count[person] = 0
    results = []
    zf = zipfile.ZipFile(person_dir + '.zip', 'r')
    for f_name in zf.namelist():
        sakuhin = f_name.encode('cp437').decode('cp932')
        print(person, sakuhin)
        sakuhin_count[person] += 1
        sakuhin_file = person_dir + '/' + sakuhin
        try:
            fp = zf.open(f_name, 'r')
            bindata = fp.read()
            text = bindata.decode('shift_jis')
            lines = tokenize(text)
            results += lines
        except Exception as e:
            print('[error]', sakuhin_file, e)
            continue
    fname = './text/' + person + '.wakati'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(results))
    print(person)

print('作品数:', sakuhin_count)
