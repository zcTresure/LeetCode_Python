# -*- coding: utf-8 -*-
# File:      2194. Excel 表中某个范围内的单元格.py
# DATA:      2022/5/30
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for row in range(ord(s[0]), ord(s[3]) + 1):
            for col in range(int(s[1]), int(s[4]) + 1):
                ans.append(chr(row) + str(col))
        return ans


print(Solution().cellsInRange(s="K1:L2"))
print(Solution().cellsInRange(s="A1:F1"))
