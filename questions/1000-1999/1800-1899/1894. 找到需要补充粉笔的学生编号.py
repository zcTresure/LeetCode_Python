# -*- coding: utf-8 -*-
# File:      1894. 找到需要补充粉笔的学生编号.py
# DATA:      2021/9/10
# Software:  PyCharm
__author__ = 'zcFang'

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


chalk = [3,4,1,2]
k = 25
print(Solution().chalkReplacer(chalk, k))
