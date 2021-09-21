# -*- coding: utf-8 -*-
# File:      58. 最后一个单词的长度.py
# DATA:      2021/9/21
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                ans += 1
            elif ans:
                return ans
        return ans


s = "sakjdo aksdnjla alskjdl asldj laskkjgwn ejorfi"
print(Solution().lengthOfLastWord(s))
