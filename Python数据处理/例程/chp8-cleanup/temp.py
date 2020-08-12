a = ['1', '2','3','4','5']
b = ['a', 'b','c','d','e']
c = ['甲', '乙','丙','丁','已']

zipped_data = []
for i in range(0,5,1):
    data = zip(a[i], b[i], c[i])
    print(list(data))
    zipped_data.append(data)

unzipped_data = list(zipped_data)

set_of_keys = set([
     '%s-%s-%s' % (x[0], x[1], x[2]) for x in unzipped_data])

print(set_of_keys)
