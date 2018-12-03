def get_class(x):
    """
    x: index
    """
    # Example
    distribution = [0, 2000, 4000, 6000, 8000, 10000]
    x_class = 0
    for i in range(len(distribution)):
        if x > distribution[i]:
            x_class += 1
    return x_class


def kmeans_purity(labels):
    """
    labels: (n samples,)
    """
    dic = {}
    # Number of clusters
    n = 5
    for i in range(n):
        dic[i] = {}
    for i in range(len(labels)):
        cluster = labels[i]
        i_class = get_class(i)
        old_count = dic.get(cluster).get(i_class, 0)
        dic[cluster][i_class] = old_count + 1
    percent = {}
    totals = {}
    for k in dic:
        _max = 0
        total = 0
        for c in dic[k]:
            total += dic[k][c]
            _max = max(_max, dic[k][c])
        if total == 0:
            percent[k] = -1
        else:
            percent[k] = _max / total
        totals[k] = total
    return percent, totals
