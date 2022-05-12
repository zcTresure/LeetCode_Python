# -*- coding: utf-8 -*-
# File:      942. 增减字符串匹配.py
# DATA:      2022/5/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = low
                low += 1
            else:
                perm[i] = high
                high -= 1
        perm[n] = low
        return perm


print(Solution().diStringMatch(s='IDID'))
