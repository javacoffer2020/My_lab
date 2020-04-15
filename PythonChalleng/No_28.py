def level_28() -> None:
    print(f"\033[31mLevel 28\033[0m")
    from PIL import Image
    im = Image.open("source/bell.png")
    green = list(im.split()[1].getdata())
    diff = [abs(p1 - p2) for p1, p2 in zip(green[0::2], green[1::2])]
    diff_filter = list(filter(lambda x: x != 42, diff))
    text = bytes(diff_filter).decode()
    print(text)


if __name__ == "__main__":
    level_28()