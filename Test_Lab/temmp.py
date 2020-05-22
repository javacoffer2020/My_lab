import sys
sys.setrecursionlimit(100000)  # 设置递归的最大限制次数为100000次


# 递归partition函数
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 第一步：找右边比左边tmp小的数，移动右边index
            right = right - 1  # 往左走一步
        li[left] = li[right]  # 第二步：把右边的数写到左边的位置上来
        # print(li,"right")
        while left < right and li[left] <= tmp:  # 第三步：找左边比起大的数，移动左边index
            left = left + 1
        li[right] = li[left]  # 第四步 左边移到右边
        # print(li,"left")
    li[left] = tmp  # 把tmp归位
    return left


# 快速排序算法的整体主框架函数
def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)  # 获得所定元素应该所处的位置
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


li = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort(li)
print(li)