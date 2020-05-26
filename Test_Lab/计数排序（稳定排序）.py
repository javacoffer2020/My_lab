def count_sort_2(array=[]):
    # 1.得到数列的最大值、最小值，并计算出差值d
    max_value = array[0]
    min_value = array[0]
    for i in range(1,len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 2.创建统计数组并统计对应元素个数
    count_array = [0] * (d+1)
    for i in range(0,len(array)):
        count_array[array[i]-min_value] += 1
    # 3.统计数组做变形，后的元素等于前面的元素之和
    for i in range(1, len(array)):
        count_array[i] += count_array[i-1]
    # 4.倒叙遍历原始数列，从统计数组找到正确位置，输出到结果数组
    sorted_array = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        sorted_array[count_array[array[i]-min_value]-1] = array[i]
        count_array[array[i] - min_value] -= 1
    return sorted_array


my_array = list([95,94,91,98,99,90,99,93,91,92])
print(count_sort_2(my_array))