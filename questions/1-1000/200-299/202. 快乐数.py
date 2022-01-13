# -*- coding: utf-8 -*-
# File:    202. 快乐数.py
# Date:    2022/1/10
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def isHappy(self, n: int) -> bool:

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1


n = 19
print(Solution().isHappy(n))
