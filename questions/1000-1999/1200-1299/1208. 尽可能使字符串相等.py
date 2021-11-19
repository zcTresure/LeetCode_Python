# Date:       2021/2/8
# encode:      UTF-8
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

    # 滑动窗口
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        # 两个字符串的差值大小构建一个差值数组
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        maxLength = start = end = 0
        total = 0
        while end < n:
            # 当前窗口的所需的最大cost
            total += diff[end]
            # 窗口内cost过大，窗口左端右移
            while total > maxCost:
                total -= diff[start]
                start += 1
            # 更新最大窗口长度
            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength


test = Solution()
s = 'abcdaabc'
t = 'bcdeaabd'
maxCost = 3
print(test.equalSubstring(s, t, maxCost))
