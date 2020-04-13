import time

start = time.time()
a = ['1']

def new_num(a=0):
    nl = list(str(a))
    nl += ('a')
    nl_new = list()
    count = 1
    for i in range(1, len(nl)):
        if nl[i] == nl[i-1]:
            count +=1
        else:
            nl_new += (str(count), nl[i-1])
            count = 1
    return ''.join(nl_new)


for i in range(1,31):
    a.append(new_num(a[i-1]))

print(len(a[30]))

end = time.time()
print(end - start)
