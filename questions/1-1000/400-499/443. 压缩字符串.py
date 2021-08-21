# -*- coding: utf-8 -*-
# File:      443. 压缩字符串.py
# DATA:      2021/8/21
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 双指针
    def compress(self, chars: List[str]) -> int:
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        n = len(chars)
        write = left = 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    anchor = write
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    reverse(anchor, write -1)
                    # print(chars)
                left = read + 1
        return write


# chars = ["a", "a", "b", "b", "c", "c", "c"]
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(Solution().compress(chars))
