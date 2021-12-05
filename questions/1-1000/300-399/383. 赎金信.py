# -*- coding: utf-8 -*-
# File:      383. 赎金信.py
# DATA:      2021/12/4
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not Counter(ransomNote) - Counter(magazine)


rangsomNote = "aacc"
magazine = "aacddc"
print(Solution().canConstruct(rangsomNote, magazine))
