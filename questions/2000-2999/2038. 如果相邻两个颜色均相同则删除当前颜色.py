# -*- coding: utf-8 -*-
# File:      2038. 如果相邻两个颜色均相同则删除当前颜色.py
# DATA:      2022/3/22
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = '#', 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[ord(c) - ord('A')] += 1
        return freq[0] > freq[1]


print(Solution().winnerOfGame("AAABABB"))
