import zipfile
import re

z = zipfile.ZipFile('./source/channel.zip', 'r')

nextfile = '90052.txt'
comments = []
count = 1

while (1):
    information = z.read(nextfile)
    comments.append(z.getinfo(nextfile).comment)
    information = str(information, encoding='utf-8')
    print(count, information)
    result = re.findall("[0-9]", information)
    if len(result) > 0:
        convert = ''.join(result)
        nextfile = convert+'.txt'
        count += 1
    else:
        break

end = ""
for list in comments:
    end += str(list, encoding="utf-8")
print(end)


