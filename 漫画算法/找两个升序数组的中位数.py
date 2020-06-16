def find_median_sorted_arrays(array_A, array_B):
    m,n = len(array_A), len(array_B)
    # 如果数组A的长度大于等于数组B的长度，则交换数组
    if m>n:
        array_A, array_B, m, n = array_B, array_A, n, m
    if n == 0:
        raise ValueError
    start, end, half_len = 0, m, (m+n+1)//2
    while start <= end:
        i = (start + end) // 2
        j = half_len - i
        if i<m and array_B[j-1] > array_A[i]:
            # i偏小了，需要右移
            start = i + 1
        