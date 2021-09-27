# -*- coding: utf-8 -*-
# File:      639. 解码方法 II.py
# DATA:      2021/9/27
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def numDecodings(self, s: str) -> int:
        def checkOneDigit(ch: str) -> int:
            if ch == '0':
                return 0
            return 9 if ch == '*' else 1

        def checkTwoDigit(ch1: str, ch2: str) -> int:
            print(ch1, ch2)
            if ch1 == '*' and ch2 == '*':
                return 15
            if ch1 == '*':
                return 2 if ch2 <= '6' else 1
            if ch2 == '*':
                if ch1 == '1':
                    return 9
                if ch1 == '2':
                    return 6
                return 0
            return ch1 != '0' and ((ord(ch1) - ord('0')) * 10 + (ord(ch2) - ord('0'))) <= 26

        a, b, c = 0, 1, 0
        mod = 1000000007
        for i in range(1, len(s) + 1):
            c = b * checkOneDigit(s[i - 1]) % mod
            if i > 1:
                print(checkTwoDigit(s[i - 2], s[i - 1]))
                c = (c + a * checkTwoDigit(s[i - 2], s[i - 1])) % mod
            b, a = c, b
            print(a, b, c)
        return c


s = '1*'
# s = '2*'
print(Solution().numDecodings(s))
