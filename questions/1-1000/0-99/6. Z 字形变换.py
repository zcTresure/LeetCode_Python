# -*- coding: utf-8 -*-
# File:      6. Z 字形变换.py
# DATA:      2022/3/1
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, row = len(s), numRows
        if row == 1 or n < row:
            return s
        ans = []
        t = row * 2 - 2
        for i in range(row):
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if 0 < i < row - 1 and j + t - i < n:
                    ans.append(s[j + t - i])
            print(ans)
        return ''.join(ans)

    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n < numRows:
            return s
        ans = []
        step = numRows * 2 - 2
        # 枚举矩阵的行
        for i in range(numRows):
            # 枚举每个周期的起始下标
            for j in range(0, n - i, step):
                # 当前周期的第一个字符
                ans.append(s[j + i])
                # 当前周期的第二个字符
                if 0 < i < numRows - 1 and j + step - i < n:
                    ans.append(s[j + step - i])
        return ''.join(ans)


print(Solution().convert(s="PAYPALISHIRING", numRows=3))
print(Solution().convert(s="PAYPALISHIRING", numRows=4))
