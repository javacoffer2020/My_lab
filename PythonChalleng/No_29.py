def level_29() -> None:
    print(f"\033[31mLevel 29\033[0m")
    import bz2
    with open("source/silence!.html", "r") as file:
        data = file.read()
    file.close()
    space_list = data.split('\n')[12:]
    count_list = [len(line) for line in space_list]
    count_bytes = bytes(count_list)
    text = bz2.decompress(count_bytes).decode()
    print(text)


if __name__ == "__main__":
    level_29()