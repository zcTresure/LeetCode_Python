# -*- coding: utf-8 -*-
# File:      1446. 连续字符.py
# DATA:      2021/12/1
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def maxPower(self, s: str) -> int:
        ans, tmp = 1, 1
        for i in range(1, len(s)):
            if (s[i] == s[i - 1]):
                tmp += 1
            else:
                ans = max(tmp, ans)
                tmp = 1
        return ans


s = "hooraaaaaaaaaaay"
print(Solution().maxPower(s))
