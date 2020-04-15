def level_21() -> None:
    print(f"\033[31mLevel 21\033[0m")
    import bz2
    import zlib
    with open("source/package.pack", "rb") as file:
        data = file.read()
    while data != b"sgol ruoy ta kool":
        if data.startswith(b"x\x9c"):
            data = zlib.decompress(data)
            print(' ', end='')
        elif data.startswith(b"BZ"):
            data = bz2.decompress(data)
            print('B', end='')
        elif data.endswith(b"\x9cx"):
            data = data[::-1]
            print()
    print()
    print(data[::-1])


if __name__ == "__main__":
    level_21()