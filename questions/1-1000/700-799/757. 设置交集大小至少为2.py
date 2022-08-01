# -*- coding: utf-8 -*-
# File:    757. 设置交集大小至少为2.py
# Date:    2022/7/22
# Software: Pycharm
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1

        return ans


print(Solution().intersectionSizeTwo(intervals=[[1, 3], [1, 4], [2, 5], [3, 5]]))
print(Solution().intersectionSizeTwo(intervals=[[1, 2], [2, 3], [2, 4], [4, 5]]))
