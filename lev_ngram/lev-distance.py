def calc_distance(a, b):
    if a == b:
        return 0
    a_len = len(a)
    b_len = len(b)
    if a == '':
        return a_len
    if b == '':
        return b_len
    matrix = [[] for i in range(a_len + 1)]
    for i in range(a_len + 1):
        # zero padding
        matrix[i] = [0 for j in range(b_len + 1)]
    for i in range(a_len + 1):
        # padding first row
        matrix[i][0] = i
    for j in range(b_len + 1):
        # padding first column
        matrix[0][j] = j
    for i in range(1, a_len + 1):
        ac = a[i - 1]
        for j in range(1, b_len + 1):
            bc = b[j - 1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                # insert
                matrix[i - 1][j] + 1,
                # delete
                matrix[i][j - 1] + 1,
                # replace
                matrix[i - 1][j - 1] + cost])
    return matrix[a_len][b_len]


print('カキトメとカンズメの距離')
print(calc_distance('カキトメ', 'カンヅメ'))

print('============================')
print('イカダからの距離')
samples = ['イカダ', 'イカスミ', 'イカ', 'サカナ', 'サンマ', 'カナダ']
base = samples[0]
r = sorted(samples, key=lambda n: calc_distance(base, n))
for n in r:
    print(calc_distance(base, n), n)
