# -*- coding: utf-8 -*-
# File:      517. 超级洗衣机.py
# DATA:      2021/9/29
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1
        ave = total // n
        ans, s = 0, 0
        for num in machines:
            num -= ave
            s += num
            ans = max(num, ans, abs(s))
        return ans


# machines = [1, 0, 5]
machines = [0, 2, 0]
# machines = [0, 3, 0]
print(Solution().findMinMoves(machines))
