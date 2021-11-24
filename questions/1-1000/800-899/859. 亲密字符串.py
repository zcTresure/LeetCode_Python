# -*- coding: utf-8 -*-
# File:      859. 亲密字符串.py
# DATA:      2021/11/23
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


s = "abc"
goal = "acb"
print(Solution().buddyStrings(s, goal))
