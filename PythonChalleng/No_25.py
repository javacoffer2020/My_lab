def level_25() -> None:
    print(f"\033[31mLevel 25\033[0m")
    from urllib import request, error
    import wave
    from PIL import Image
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, "http://www.pythonchallenge.com/", "butter", "fly")
    handler = request.HTTPBasicAuthHandler(password_mgr)
    opener = request.build_opener(handler)

    for i in range(1, 26):
        print(f"Processing {i:2d}...", end='\t')
        url = f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav"
        try:
            response = opener.open(url)
        except error.HTTPError:
            print("HTTP ERROR 404")
        else:
            with open(f"source/No_25/lake{i}.wav", "wb") as file:
                data = response.read()
                file.write(data)
                file.close()
                print("Successfully Saved.")

    im = Image.new("RGB", (300, 300))
    for i in range(1, 26):
        with wave.open(f"source/No_25/lake{i}.wav", "rb") as file:
            data = file.readframes(file.getnframes())
            file.close()
            block_im = Image.frombytes("RGB", (60, 60), data)
            x, y = (i - 1) % 5 * 60, (i - 1) // 5 * 60
            im.paste(block_im, (x, y))
    im.save("source/No_25/result.jpg")


if __name__ == "__main__":
    level_25()