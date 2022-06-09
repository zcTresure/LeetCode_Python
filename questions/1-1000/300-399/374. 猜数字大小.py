# -*- coding: utf-8 -*-
# File:     374. 猜数字大小.py
# Date:     2021/6/14
# Software: PyCharm


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
from sympy.concrete.guess import guess


# def guess(num: int) -> int:
#     return num


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid  # 答案在区间 [left, mid] 中
            else:
                left = mid + 1  # 答案在区间 [mid+1, right] 中

        # 此时有 left == right，区间缩为一个点，即为答案
        return left


print(Solution().guessNumber(n=10))
