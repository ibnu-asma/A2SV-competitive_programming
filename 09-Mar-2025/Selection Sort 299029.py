# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

l = sorted((e.start, i) for i, e in enumerate(intervals))
    res = []
    for e in intervals:
        r = bisect.bisect_left(l, (e.end,))
        res.append(l[r][1] if r < len(l) else -1)
    return res