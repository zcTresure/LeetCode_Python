# -*- coding: utf-8 -*-
# File:     12. 整数转罗马数字.py
# Date:     2021/5/14
# Software: PyCharm
__author__ = 'zcTresure'


class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [(1000, 'M'), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                         (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"), ]
        roman = []
        for value, symbol in value_symbols:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0 :
                break
        return "".join(roman)


num = int(input("输入数字: "))
test = Solution()
print(test.intToRoman(num))