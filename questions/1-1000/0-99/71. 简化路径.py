# -*- coding: utf-8 -*-
# File:      71. 简化路径.py
# DATA:      2022/1/6
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        stack = []
        for name in names:
            if name == '..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        return "/" + "/".join(stack)


path = "/home/"
print(Solution().simplifyPath(path))
