# -*- coding: utf-8 -*-
# File:      944. 删列造序.py.py
# DATA:      2022/5/12
# Software:  PyCharm
__author__ = 'zcFang'

from itertools import pairwise
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j - 1][i] > strs[j][i]:
                    ans += 1
                    print(strs[i][j - 1], strs[i][j], ans)
                    break
        return ans

    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))  # 空间复杂度为 O(m)，改用下标枚举可以达到 O(1)


strs = ['abc', 'bcd', 'cae']
strs = ["cba", "daf", "ghi"]
print(Solution().minDeletionSize(strs))
