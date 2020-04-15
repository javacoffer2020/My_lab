def level_20() -> None:
    print(f"\033[31mLevel 20\033[0m")
    from urllib import request, error
    url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
    user = "butter"
    password = "fly"
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, user, password)
    handler = request.HTTPBasicAuthHandler(password_mgr)
    opener = request.build_opener(handler)
    #
    # # start = -1
    # # start = 2123456790
    # start = 1152983632
    # for _ in range(100):
    #     # start += 1     # this is for start = -1
    #     start -= 1   # this is for start = 2123456790 and start = 1152983632
    #     print(f"{start}", end="\t")
    #     opener.addheaders = [("range", f"bytes={start}-"), ]
    #     try:
    #         response = opener.open(url,timeout=30)
    #     except error.HTTPError:
    #         print("HTTP Error 416")
    #     else:
    #         data = response.read()
    #         headers = dict(response.info())
    #         content_range = str(headers['Content-Range'])
    #         print(f"\033[31m{content_range}\t{data}\033[0m")
    #         # start = int(content_range.split('-')[1].split('/')[0])     # this is for start = -1
    #         start = int(content_range.split(' ')[1].split('-')[0])   # this is for start = 2123456790 and start = 1152983632

    with open("source/invader.zip", "wb") as file:
        opener.addheaders = [("range", f"bytes=1152983631-"), ]
        response = opener.open(url)
        data = response.read()
        file.write(data)


if __name__ == "__main__":
    level_20()

# start from begin position
#
# 0	    bytes     0-30202/2123456789    b'\xff\xd8\xff\............\xa3\xff\xd9'
# 30203	bytes 30203-30236/2123456789	b"Why don't you respect my privacy?\n"
# 30237	bytes 30237-30283/2123456789	b'we can go on in this way for really long time.\n'
# 30284	bytes 30284-30294/2123456789	b'stop this!\n'
# 30295	bytes 30295-30312/2123456789	b'invader! invader!\n'
# 30313	bytes 30313-30346/2123456789	b'ok, invader. you are inside now. \n'

# start from end position
#
# 2123456789	bytes 2123456744-2123456788/2123456789	b'esrever ni emankcin wen ruoy si drowssap eht\n'
# 2123456743	bytes 2123456712-2123456743/2123456789	b'and it is hiding at 1152983631.\n'

# start from 1152983631
#
# 1152983631	bytes 1152983631-1153223363/2123456789	b'PK\x03\x04\x14\............\x00\x00\x00'