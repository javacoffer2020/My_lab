from PIL import Image
import math

img = Image.open('source/wire.png')
width = height = (int)(math.sqrt(img.size[0]))
newpic = Image.new("RGB", (width, height))
length = img.size[0]
counter = 0
layer = 0

while counter < length:

    for i in range(layer, width - layer):
        pixel = img.getpixel((counter, 0))
        counter += 1
        newpic.putpixel((i, layer), pixel)

    for i in range(layer + 1, height - layer):
        pixel = img.getpixel((counter, 0))
        counter += 1
        newpic.putpixel((width - layer - 1, i), pixel)

    for i in range(width - layer - 2, layer - 1, -1):
        pixel = img.getpixel((counter, 0))
        counter += 1
        newpic.putpixel((i, height - layer - 1), pixel)

    for i in range(height - layer - 2, layer, -1):
        pixel = img.getpixel((counter, 0))
        counter += 1
        newpic.putpixel((layer, i), pixel)

    layer += 1

newpic.show()
