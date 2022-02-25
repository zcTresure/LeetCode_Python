# -*- coding: utf-8 -*-
# File:      537. 复数乘法.py
# DATA:      2022/2/25
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def strToInt(s: str) -> list:
            ans = []
            tmp = 0
            flag = False
            for ch in s:
                if ch == '-':
                    flag = True
                elif '0' <= ch <= '9':
                    tmp = tmp * 10 + int(ch)
                else:
                    if flag:
                        tmp = -tmp
                        flag = False
                    ans.append(tmp)
                    tmp = 0
            return ans

        nums1 = strToInt(num1)
        nums2 = strToInt(num2)
        a = nums1[0] * nums2[0] - nums1[1] * nums2[1]
        b = nums1[0] * nums2[1] + nums1[1] * nums2[0]
        return str(a) + "+" + str(b) + "i"

    # map模拟
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'


print(Solution().complexNumberMultiply(num1="1+1i", num2="1+1i"))
