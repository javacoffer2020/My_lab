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


def remove_k_digits_v2(num, k):
    # 新整数的最终长度 = 原整数长度 - k
    new_length = len(num) - k
    # 创建一个栈，用于接收所有的数字
    stack =[]
    for i in range(0,len(num)):
        # 遍历当前数字
        c = num[i]
        # 当栈顶数字大于遍历到的当前数字时，栈顶数字出栈（相当于删除数字）
        while len(stack) > 0 and stack[len(stack)-1] > c and k>0:
            stack.pop()
            k -=1
        # 当遇到数字0，且栈为空，0不入栈
        if '0' == c and len(stack) == 0:
            new_length -= 1
            if new_length <= 0:
                return "0"
            continue
        # 遍历到的当前数字入栈
        stack.append(c)
    # 找到栈中第一个非零数字的位置，以此构建新的整数字符串
    if new_length <= 0:
        return "0"
    return "".join(stack)


print(remove_k_digits_v2("1593212", 1))
print(remove_k_digits_v2("30200", 1))
print(remove_k_digits_v2("10", 3))