# -*- coding: utf-8 -*-
# File:      1021. 删除最外层的括号.py
# DATA:      2021/9/13
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        level = 1
        for c in s:
            if c == ')':
                level -= 1
            if level > 1:
                ans = ans + c
            if c == '(':
                level += 1
        return ans


s = '(()())(())'
print(Solution().removeOuterParentheses(s))