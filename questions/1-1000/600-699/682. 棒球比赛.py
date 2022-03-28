# -*- coding: utf-8 -*-
# File:      682. 棒球比赛.py
# DATA:      2022/3/26
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        tmp = 0
        for s in ops:
            if s == "+":
                scores.append(scores[-1] + scores[-2])
            elif s == "C":
                tmp = scores[-1]
                scores.pop()
            elif s == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(s))
            print(scores)
        return sum(scores)


ops = ["5", "2", "C", "D", "+"]
print(Solution().calPoints(ops))
ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(ops))
