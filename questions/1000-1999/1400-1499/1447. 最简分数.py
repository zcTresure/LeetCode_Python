# -*- coding: utf-8 -*-
# File:    1447. 最简分数.py
# Date:    2022/2/13
# Software: Pycharm
__author__ = 'zcFang'

from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{numerator}/{denominator}" for denominator in range(2, n + 1) for numerator in range(1, denominator)
                if gcd(denominator, numerator) == 1]


print(Solution().simplifiedFractions(n=4))
