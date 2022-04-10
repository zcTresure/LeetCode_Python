# -*- coding: utf-8 -*-
# File:      796. 旋转字符串.py
# DATA:      2022/4/7
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if m != n:
            return False
        for i in range(n):
            for j in range(n):
                if s[(i + j) % n] != goal:
                    break
            else:
                return True
        return False

    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


print(Solution().rotateString(s='abcde', goal='bcdea'))
