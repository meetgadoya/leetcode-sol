def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    sorted_d = {}
    for num in nums:
        # print(num)
        if num in d.keys():
            d[num] += 1
        else:
            d.update({num: 1})
    # print("HEY",d)

    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    # print(sorted_d)
    e = []
    l = len(sorted_d)
    while (k > 0):
        e.append(sorted_d[l - 1][0])
        l = l - 1
        k = k - 1
    return e
