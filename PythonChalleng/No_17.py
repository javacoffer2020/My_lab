def level_17() -> None:
    from urllib import request, parse
    from http import cookiejar
    from xmlrpc.client import ServerProxy
    import bz2

    def crawl():
        epochs = 0
        busynothing = "12345"
        info = ""
        while str.isdigit(busynothing):
            epochs += 1
            url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}"
            cookie = cookiejar.MozillaCookieJar()
            handler = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(handler)
            response = opener.open(url)
            text = response.read().decode()
            print(f"{epochs:<3d}\tbusynothing = {busynothing}\n\t{text}")
            for c in cookie:
                print(f"\t{c.name} = {c.value}")
                if c.name == "info":
                    info += c.value
            busynothing = str(text.split(' ')[-1])
        print(info.encode())

    def decompress():
        info = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA" + \
               "%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS" + \
               "%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
        info = info.replace("+", "%20")
        info = parse.unquote_to_bytes(info)
        info = bz2.decompress(info).decode()
        print(info)

    def phone():
        server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
        response = server.phone("Leopold")
        print(response)

    print(f"\033[31mLevel 17\033[0m")
    crawl()
    decompress()
    phone()


if __name__ == "__main__":
    level_17()

# busynothing = 12345 -> epochs = 118 , busynothing = 83051
#
# 1  	busynothing = 12345
# 	    If you came here from level 4 - go back!<br>You should follow the obvious chain...<br><br>and the next busynothing is 44827
# 	    info = B
# 2  	busynothing = 44827
# 	    and the next busynothing is 45439
# 	    info = Z
# ...... ...... ...... ...... ...... ......
# 117	busynothing = 96070
# 	    and the next busynothing is 83051
# 	    info = %24
# 118	busynothing = 83051
# 	    that's it.
# 	    info = %90
# b'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'


# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.


# 555-VIOLIN