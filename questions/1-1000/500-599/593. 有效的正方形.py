# -*- coding: utf-8 -*-
# File:    593. 有效的正方形.py
# Date:    2022/8/1
# Software: Pycharm
from typing import List, Tuple


def checkLength(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]


def checkMidPoint(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]


def calCos(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[0] + v1[1] * v2[1]


def help(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p4[0], p3[1] - p4[1])
    return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        if help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if help(p1, p4, p2, p3):
            return True
        return False


print(Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
