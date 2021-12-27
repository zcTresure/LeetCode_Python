# -*- coding: utf-8 -*-
# File:    409. 最长回文串.py
# Date:    2021/12/27
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = Counter(s)
        for val in count.values():
            ans += val // 2 * 2
            if ans % 2 == 0 and val % 2 == 1:
                ans += 1
        return ans


s = 'asudhasnhagsdjajdhajdhjasdkj'
print(Solution().longestPalindrome(s))
