# Date:       2021/2/8
# Coding:      UTF-8
__author__ = "zcTresure"

from itertools import accumulate
from bisect import bisect_left


class Solution:
    # 前缀和 + 二分查找
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        accDiff = [0] + list(accumulate(abs(ord(sc) - ord(st)) for sc, st in zip(s, t)))
        maxLength = 0
        for i in range(1, n + 1):
            start = bisect_left(accDiff, accDiff[i] - maxCost)
            maxLength = max(maxLength, i - start)

        return maxLength

    # 双指针
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        maxLength = start = end = 0
        total = 0
        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength


test = Solution()
s = 'abcdaabc'
t = 'bcdeaabd'
maxCost = 3
print(test.equalSubstring(s, t, maxCost))
