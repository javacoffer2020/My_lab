f = open("./source/evil2.gfx",'rb')
content = f.read()
f.close()

for i in range(5):
    f = open('./source/No_12/%d.jpg' % i, 'wb')
    f.write(content[i::5])
    f.close()

print('Finished')


import io
from PIL import Image

with open("./source/evil2.gfx", "rb") as f:
    data = f.read()

for i in range(5):
    piece = data[i::5]
    im = Image.open(io.BytesIO(piece))
    with open("./source/No_12/2_%d.%s" % (i, im.format.lower()), "wb") as f:
        f.write(piece)

print('Finished')