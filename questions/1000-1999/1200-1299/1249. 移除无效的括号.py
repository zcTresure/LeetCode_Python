# -*- coding: utf-8 -*-
# File:      1249. 移除无效的括号.py
# DATA:      2022/1/4
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                index.add(i)
            else:
                stack.pop()
        index = index.union(set(stack))
        string = []
        for i, c in enumerate(s):
            if i not in index:
                string.append(c)
        return "".join(string)


s = "leet(()c))o(d))e)"
print(Solution().minRemoveToMakeValid(s))
