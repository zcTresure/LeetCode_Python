# Date:       2020/12/31
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        print(intervals)
        right, ans = intervals[0][1], 1
        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        return n - ans


test = Solution()
intervals = [[1, 2], [1, 2], [1, 2]]
print(test.eraseOverlapIntervals(intervals))
