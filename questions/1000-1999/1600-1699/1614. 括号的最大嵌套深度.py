# -*- coding: utf-8 -*-
# File:      1614. 括号的最大嵌套深度.py
# DATA:      2022/1/7
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if (c == '('):
                cnt += 1
                ans = max(ans, cnt)
            elif c == ')':
                cnt -= 1
            else:
                continue
        return ans


s = "(1+(2*3)+((8)/4))+1"
print(Solution().maxDepth(s))
