def level_18() -> None:
    print(f"\033[31mLevel 18\033[0m")
    import gzip
    import difflib
    from PIL import Image
    from io import BytesIO

    # decompress and split data
    data1_list, data2_list = [], []
    with gzip.open("source/deltas.gz", "rb") as file:
        for data in file:
            data = data.decode("utf-8")
            data1, data2 = data[:53].rstrip(' ') + "\n", data[56:]
            if data1 != "\n":
                data1_list.append(data1)
            if data2 != "\n":
                data2_list.append(data2)

    # Differ()
    d = difflib.Differ()
    diff = d.compare(data1_list, data2_list)
    diff_date = list(diff)



    # group data
    space_bytes, plus_bytes, minus_bytes = b"", b"", b""
    for data in diff_date:
        data_list = data[2:].strip('\n').split(' ')
        byte = bytes([int(i, 16) for i in data_list])
        if data[0] == '+':
            plus_bytes += byte
        elif data[0] == '-':
            minus_bytes += byte
        elif data[0] == ' ':
            space_bytes += byte

    # save image

    stream = BytesIO(space_bytes)
    image_space = Image.open(stream)
    image_space.save("source/No_18/space.png")

    stream = BytesIO(plus_bytes)
    image_space = Image.open(stream)
    image_space.save("source/No_18/plus.png")

    stream = BytesIO(minus_bytes)
    image_space = Image.open(stream)
    image_space.save("source/No_18/minus.png")


if __name__ == "__main__":
    level_18()