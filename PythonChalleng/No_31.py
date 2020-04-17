def level_31() -> None:
    print(f"\033[31mLevel 31\033[0m")
    from PIL import Image

    left, top, width, height = 0.34, 0.57, 0.036, 0.027
    im0 = Image.open("source/mandelbrot.gif")
    im1 = Image.new("P", (640, 480))
    im1.putpalette(im0.getpalette())
    for w in range(640):
        for h in range(480):
            z = complex(0, 0)
            c = complex(left + w * width / 640, top + (479 - h) * height / 480)
            for i in range(1, 128):
                z = z ** 2 + c
                if abs(z) > 2:
                    im1.putpixel((w, h), i - 1)
                    break
            else:
                im1.putpixel((w, h), 127)
    im1.show

    data0, data1 = list(im0.getdata()), list(im1.getdata())
    diff = [255 * (p0 < p1) for p0, p1 in zip(data0, data1) if p0 != p1]
    im2 = Image.new("L", (23, 73))
    im2.putdata(diff)
    im2.show()


if __name__ == "__main__":
    level_31()