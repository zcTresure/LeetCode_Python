# -*- coding: utf-8 -*-
# File:      187. 重复的DNA序列.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans
