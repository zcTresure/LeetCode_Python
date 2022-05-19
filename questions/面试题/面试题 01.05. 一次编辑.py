# -*- coding: utf-8 -*-
# File:      面试题 01.05. 一次编辑.py
# DATA:      2022/5/13
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 分情况讨论
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            first, second = second, first
            m, n = n, m
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                print(first[i + 1:], second[i + 1:])
                print(first[i + 1:], second[i:])
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True


first = "teacher"
second = "treacher"

print(Solution().oneEditAway(first, second))
