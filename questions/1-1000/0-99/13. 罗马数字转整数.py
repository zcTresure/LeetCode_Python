# -*- coding: utf-8 -*-
# File:     13. 罗马数字转整数.py
# Date:     2021/5/15
# Software: PyCharm
__author__ = 'zcTresure'


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = symbols_value[ch]
            if i < n - 1 and value < symbols_value[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


s = input("输入罗马数字：")
test = Solution()
print(test.romanToInt(s))
