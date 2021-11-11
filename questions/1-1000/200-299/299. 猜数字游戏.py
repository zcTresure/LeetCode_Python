# -*- coding: utf-8 -*-
# File:      299. 猜数字游戏.py
# DATA:      2021/11/8
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f'{bulls}A{cows}B'


secret = "1807"
guess = "7810"
print(Solution().getHint(secret, guess))
