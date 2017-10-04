import pandas as pd

tbl = pd.DataFrame({
    'weight': [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
    'height': [170, 180, 155, 143, 154, 160],
    'type': ['f', 'n', 'n', 't', 't', 'f']
})

print('tbl[2:4]\n', tbl[2:4])
print('tbl[3:]\n', tbl[3:])
