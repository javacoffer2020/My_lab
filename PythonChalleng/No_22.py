def level_22() -> None:
    print(f"\033[31mLevel 22\033[0m")
    from PIL import Image, ImageSequence
    im0 = Image.open("source/white.gif")
    im1 = Image.new("1", (400, 100))
    index = 1
    x, y = 50, 50
    for frame in ImageSequence.Iterator(im0):
        i, j = 98, 98
        while i <= 102:
            if frame.getpixel((i, j)) != 0:
                break
            if j == 102:
                i, j = i + 1, 98
            else:
                j += 1
        dx, dy = i - 100, j - 100
        if dx == dy == 0:
            index += 1
            x, y = index * 50, 50
        else:
            x, y = x + dx, y + dy
            im1.putpixel((x, y), 1)
    im1.show()


if __name__ == "__main__":
    level_22()