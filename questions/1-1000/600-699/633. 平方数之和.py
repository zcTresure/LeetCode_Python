# File Name:  633. 平方数之和
# date:       2021/4/28
# encode:      UTF-8
__author__ = 'zcTresure'

from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        target = int(sqrt(c) + 1)
        for i in range(target):
            if sqrt(c - i * i) == int(sqrt(c - i * i)):
                return True
        return False
