# -*- coding: utf-8 -*-
# File:      997. 找到小镇的法官.py
# DATA:      2021/12/19
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = Counter(y for _, y in trust)
        out_degrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if in_degrees[i] == n - 1 and out_degrees[i] == 0), -1)
