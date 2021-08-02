# -*- coding: utf-8 -*-
# File:      171. Excel 表列序号.py
# DATA:      2021/8/2
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number, multiple = 0, 1
        for i in range(len(columnTitle) - 1, -1, -1):
            k = ord(columnTitle[i]) - ord("A") + 1
            number += k * multiple
            multiple *= 26
        return number


columnTitle = "AB"
print(Solution().titleToNumber(columnTitle))
