def remove_k_digits(num, k):
    for i in range(0, k):
        has_cut = False
        # 从左向右遍历，找到比自己右侧数字大的数字并删除
        for j in range(0, len(num)-1):
            if num[j] > num[j+1]:
                num = num[0:j] + num[j+1:len(num)]
                has_cut = True
                break
        # 如果没有找到要删除的数字，则删除最后一个数字
        if not has_cut:
            num = num[0:len(num)-1]
    # 清除整数左边的数字0
    for j in range(0, len(num)-1):
        if num[0] != '0':
            break
        num =num[1:len(num)]
    if len(num) == 0:
        return "0"
    return num


print(remove_k_digits("1593212", 1))
print(remove_k_digits("30200", 1))
print(remove_k_digits("10", 3))