# -*- coding: utf-8 -*-
# File:      821. 字符的最短距离.py
# DATA:      2022/4/19
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        index = -n
        for i, ch in enumerate(s):
            if str(ch) == c:
                index = i
            ans[i] = i - index

        index = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                index = i
            ans[i] = min(ans[i], index - i)
        return ans


print(Solution().shortestToChar(s="loveleetcode", c="e"))
