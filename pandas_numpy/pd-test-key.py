import pandas as pd

tbl = pd.DataFrame({
    'weight': [80.0, 70.4, 65.5, 45.9, 51.2],
    'height': [170, 180, 155, 143, 154],
    'type': ['f', 'n', 'n', 't', 't']
})

print('体重の一覧')
print(tbl['weight'])

print('体重と身長の一覧')
print(tbl[['weight', 'height']])
