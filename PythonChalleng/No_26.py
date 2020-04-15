def level_26() -> None:
    print(f"\033[31mLevel 26\033[0m")
    import hashlib
    with open("source/mybroken.zip", "rb") as file:
        broken_data = file.read()
    file.close()
    correct_digest = "bbb8b499a0eef99b52c7f13f4e78c24b"
    for pos in range(len(broken_data)):
        print(f"Trying position {pos} ...")
        for k in range(256):
            data = broken_data[:pos] + bytes([k]) + broken_data[pos + 1:]
            digest = hashlib.md5(data).hexdigest()
            if digest == correct_digest:
                print(f"Successfully insert {k} at position {pos}")
                with open("source/mycorrect.zip", "wb") as file:
                    file.write(data)
                file.close()
                return


if __name__ == "__main__":
    level_26()

# Level 26
# Trying position 0 ...
# Trying position 1 ...
# Trying position 2 ...

# Trying position 1234 ...
# Successfully insert 168 at position 1234