# -*- coding: utf-8 -*-
# File:     168. Excel表列名称.py
# Date:     2021/6/29
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber:
            columnNumber -= 1
            ans.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(ans[::-1])


print(Solution().convertToTitle(701))
