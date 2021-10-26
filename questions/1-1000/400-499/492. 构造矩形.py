# -*- coding: utf-8 -*-
# File:      492. 构造矩形.py
# DATA:      2021/10/23
# Software:  PyCharm
__author__ = 'zcFang'

from math import sqrt
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(sqrt(area))
        while area % width:
            width -= 1
        return [area // width, width]


area = 4
print(Solution().constructRectangle(area))
