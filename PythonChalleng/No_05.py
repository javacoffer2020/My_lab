import pickle

pk_file = open('.//source//banner.p', 'rb')
data = pickle.load(pk_file)
for line in data:
    for chr in line:
        x, y = chr
        print(x*y, end='')

    print('')

