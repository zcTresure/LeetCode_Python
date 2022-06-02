# -*- coding: utf-8 -*-
# File:      241. 为运算表达式设计优先级.py
# DATA:      2022/6/1
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


print(Solution().diffWaysToCompute("1-2-3-4"))
