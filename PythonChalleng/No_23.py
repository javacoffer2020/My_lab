def level_23() -> None:
    print(f"\033[31mLevel 23\033[0m")
    import this
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = "va gur snpr bs jung?"
    for offset in range(26):
        new_aplhabets = alphabets[offset:] + alphabets[:offset]
        trans = str.maketrans(alphabets, new_aplhabets)
        new_text = text.translate(trans)
        print(new_text)


if __name__ == "__main__":
    level_23()