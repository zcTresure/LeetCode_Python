# -*- coding: utf-8 -*-
# File:      面试题 16.26. 计算器.py
# DATA:      2022/5/28
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def calculate(self, s: str) -> int:
        tmp = num1 = num2 = 0
        s = s + '#'
        prev_o = "+"
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():  # 数字
                tmp = tmp * 10 + int(c)
            else:
                if prev_o in '+-':
                    num1 += num2
                    num2 = tmp if prev_o == '+' else -tmp
                elif prev_o == '*':
                    num2 *= tmp
                else:  # 负数除法下取整
                    if num2 > 0:
                        num2 //= tmp
                    else:
                        num2 = -num2 // tmp
                        num2 = -num2
                prev_o = c
                tmp = 0
        return num1 + num2


s = " 14-3/2 "
print(Solution().calculate(s))
print(-3 // 2)
