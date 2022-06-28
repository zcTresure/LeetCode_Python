# -*- coding: utf-8 -*-
# File:      522. 最长特殊序列 II.py
# DATA:      2022/6/27
# Software:  PyCharm
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def sub_str(s: str, t: str) -> int:
            ls = lt = 0
            while ls < len(s) and lt < len(t):
                if s[ls] == t[lt]:
                    ls += 1
                lt += 1
            return ls == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and sub_str(strs[i], strs[j]):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))
        return ans
