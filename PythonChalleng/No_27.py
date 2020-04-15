def level_27() -> None:
    print(f"\033[31mLevel 27\033[0m")
    from PIL import Image
    import bz2
    import keyword
    im0 = Image.open("source/zigzag.gif")
    palette = im0.getpalette()[::3]
    data = im0.tobytes()
    palette_bytes = bytes(palette)
    index_bytes = bytes([i for i in range(256)])
    trans = bytes.maketrans(index_bytes, palette_bytes)
    new_data = data.translate(trans)

    print(data)
    print(new_data)

    diff_bytes = b''.join([bytes([b1]) if b1 != b2 else b'' for b1, b2 in zip(data[1:], new_data[:-1])])
    text = bz2.decompress(diff_bytes).decode()
    content = set(s if not keyword.iskeyword(s) else '' for s in text.split(' '))
    print(content)


if __name__ == "__main__":
    level_27()

# Level 27
# b'\xd7\xd0\xcb\x0c\...\xd49\xb8\x17N\xfad'
#     b'\xd0\xcb\x0c\...\xd49\xb8\x17N\xfad]'
# {'', 'repeat', 'switch', 'print', '../ring/bell.html', 'exec'}