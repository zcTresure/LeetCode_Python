# -*- coding: utf-8 -*-
# File:    1332. 删除回文子序列.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


print(Solution().removePalindromeSub(s="abb"))
