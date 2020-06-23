def get_best_gold_mining(w, p=[], g=[]):
    """
    :param w: 工人数量
    :param p: 金矿开采所需工人数量
    :param g: 金矿储量
    :return: 最优收益
    """
    # 创建当前结果
    results = [0]*(w+1)
    # 充填一位数组
    for i in range(1, len(g)+1):
        for j in range(w, 0, -1):
            if j>= p[i-1]:
                results[j] = max(results[j], results[j-p[i-1]] + g[i-1])
    # 返回最后一个格子的值
    return results[w]

p = list([5,5,3,4,3])
g = list([400, 500, 200, 300, 350])
print(get_best_gold_mining(10,p,g))
