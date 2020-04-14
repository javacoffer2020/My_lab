from PIL import Image

origin = Image.open("./source/cave.jpg")

width, height = origin.size

odd = Image.new(origin.mode, (width//2, height//2))
even = Image.new(origin.mode, (width//2, height//2))

for x in range(width):
    for y in range(height):
        if(x+y) % 2 == 0:
            odd.putpixel((x//2, y//2), origin.getpixel((x, y)))
        else:
            even.putpixel((x//2, y//2), origin.getpixel((x, y)))

odd.show()
even.show()
