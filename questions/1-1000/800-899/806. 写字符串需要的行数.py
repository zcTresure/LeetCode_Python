# -*- coding: utf-8 -*-
# File:      806. 写字符串需要的行数.py
# DATA:      2022/4/12
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 直接遍历
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, width = 1, 0
        for ch in s:
            need = widths[ord(ch) - ord('a')]
            width += need
            if width > 100:
                width = need
                lines += 1

        return [lines, width]


widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "abcdefghijklmnopqrstuvwxyz"
print(Solution().numberOfLines(widths, S))
widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "bbbcccdddaaa"
print(Solution().numberOfLines(widths, S))
