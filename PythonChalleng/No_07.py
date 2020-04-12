from PIL import Image

img = Image.open("./source/oxygen.png")
data = img.convert('L').getdata()
msg = ''
for i in range(3, 608, 7):
    msg += chr(data[img.size[0]*50+i])

print(msg)z

msg2 = ''
for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    msg2 += chr(i)

print(msg2)
