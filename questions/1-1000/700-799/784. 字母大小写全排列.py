# -*- coding: utf-8 -*-
# File:      784. 字母大小写全排列.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

import itertools
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(path, index):
            if index == len(s):
                ans.append(path)
                return
            if s[index].isdigit():
                dfs(path + s[index], index + 1)
            else:
                dfs(path + s[index].upper(), index + 1)
                dfs(path + s[index].lower(), index + 1)

        ans = []
        dfs("", 0)
        return ans


s = 'a1b2'
print(Solution().letterCasePermutation(s))
