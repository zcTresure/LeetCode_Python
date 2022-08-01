# -*- coding: utf-8 -*-
# File:    1374. 生成每种字符都是奇数个的字符串.py
# Date:    2022/8/1
# Software: Pycharm


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n
        return "a" * (n - 1) + "b"


print(Solution().generateTheString(n=10))
