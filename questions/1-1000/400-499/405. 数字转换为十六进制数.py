# -*- coding: utf-8 -*-
# File:      405. 数字转换为十六进制数.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'



class Solution:
    def toHex(self, num: int) -> str:
        CONV = "0123456789abcdef"
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            ans.append(num % 16)
            num //= 16
            if not num:
                break
        return "".join(CONV[n] for n in ans[::-1])


num = 26
print(Solution().toHex(num))
