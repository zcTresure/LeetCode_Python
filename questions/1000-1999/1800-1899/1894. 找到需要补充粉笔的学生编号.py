# -*- coding: utf-8 -*-
# File:      1894. 找到需要补充粉笔的学生编号.py
# DATA:      2021/9/10
# Software:  PyCharm
from bisect import bisect_right
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        ans = 0
        for i, cnt in enumerate(chalk):
            if (k < cnt):
                return i
            k -= cnt

    # 前缀和 + 二分查找
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if chalk[0] > k:
            return 0
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i - 1]
            if chalk[i] > k:
                return i
        return bisect_right(chalk, k % chalk[-1])


chalk = [3, 4, 1, 2]
k = 25
print(Solution().chalkReplacer(chalk, k))
