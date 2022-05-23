# -*- coding: utf-8 -*-
# File:      436. 寻找右区间.py
# DATA:      2022/5/20
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_left
from typing import List


class Solution:
    # 二分查找
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()
        n = len(intervals)
        ans = [-1] * n
        for _, end, id in intervals:
            i = bisect_left(intervals, [end])
            if i < n:
                ans[id] = intervals[i][2]
        return ans

    # 双指针
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts, ends = list(zip(*intervals))
        starts = sorted(zip(starts, range(n)))
        ends = sorted(zip(ends, range(n)))
        ans, j = [-1] * n, 0
        for end, id in ends:
            while j < n and starts[j][0] < end:
                j += 1
            if j < n:
                ans[id] = starts[j][1]
        return ans


print(Solution().findRightInterval(intervals=[[1, 2]]))
print(Solution().findRightInterval(intervals=[[3, 4], [2, 3], [1, 2]]))
print(Solution().findRightInterval(intervals=[[1, 4], [2, 3], [3, 4]]))
