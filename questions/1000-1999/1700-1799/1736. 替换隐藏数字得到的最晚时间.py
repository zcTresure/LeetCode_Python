# -*- coding: utf-8 -*-
# File:    1736. 替换隐藏数字得到的最晚时间.py
# Date:    2021/7/24
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def maximumTime(self, time: str) -> str:
        [a, b, _, c, d] = time
        if a == '?':
            a = '2' if b == '?' or b < '4' else '1'
        if b == '?':
            b = '3' if a == '2' else '9'
        if c == '?':
            c = '5'
        if d == '?':
            d = '9'
        return f'{a}{b}:{c}{d}'


time = "2?:?0"
print(Solution().maximumTime(time))
