def get_greastest_common_civisor(a,b):
    if a==b:
        return a
    if (a & 1) == 0 and (b & 1) == 0:
        return get_greastest_common_civisor(a >> 1, b >> 1) << 1
    elif (a & 1) == 0 and (b & 1) != 0:
        return get_greastest_common_civisor(a >> 1, b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return get_greastest_common_civisor(a, b >> 1)
    else:
        big = max(a,b)
        small = min(a,b)
        return get_greastest_common_civisor(big-small, small)


print(get_greastest_common_civisor(25, 5))
print(get_greastest_common_civisor(100 ,75))
print(get_greastest_common_civisor(900000, 3))