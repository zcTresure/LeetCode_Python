# -*- coding: utf-8 -*-
# File:      748. 最短补全词.py
# DATA:      2021/12/10
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)


licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(Solution().shortestCompletingWord(licensePlate, words))
