# -*- coding: utf-8 -*-
# File:      1576. 替换所有的问号.py
# DATA:      2022/1/5
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def modifyString(self, s: str) -> str:
        ans = list(s)
        n = len(s)
        for i in range(n):
            if ans[i] == '?':
                for b in "abc":
                    if not (i > 0 and ans[i - 1] == b or i < n - 1 and ans[i + 1] == b):
                        ans[i] = b
        return "".join(ans)


s = "?asdbias"
print(Solution().modifyString(s))
