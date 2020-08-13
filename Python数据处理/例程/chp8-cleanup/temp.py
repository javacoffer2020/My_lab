a = ['1', '2','3','4','5']
b = ['a', 'b','c','d','e']
c = ['甲', '乙','丙','丁','已']

zipped_data = []
for i in range(0,5,1):
    data = zip(a[i], b[i], c[i])
    zipped_data.append(data)

# unzipped_data = []
# for data in zipped_data:
#     unzip = data
#     unzipped_data.append(unzip)

print(zipped_data)
data1 = list(zipped_data[0])

print((data1[0])[2])
print((list(zipped_data[0])[0])[2])
# set_of_keys = set([
#      '%s-%s-%s' % ((list(x)[0])[0], (list(x)[0])[1], (list(x)[0])[2]) for x in zipped_data])
#
# print(set_of_keys)
