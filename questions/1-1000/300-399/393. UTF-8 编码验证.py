# -*- coding: utf-8 -*-
# File:      393. UTF-8 编码验证.py
# DATA:      2022/3/13
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        MASK1, MASK2 = 1 << 7, (1 << 7 | 1 << 6)

        def getBytes(num: int) -> int:
            if (num & MASK1) == 0:
                return 1
            n, mask = 0, MASK1
            while num & mask:
                n += 1
                if n > 4:
                    return -1
                mask >>= 1
            return n if n >= 2 else -1

        index, m = 0, len(data)
        while index < m:
            n = getBytes(data[index])
            if n < 0 or index + n > m or any((ch & MASK2) != MASK1 for ch in data[index + 1:index + n]):
                return False
            index += n
        return True


data = [197, 140, 1]
print(Solution().validUtf8(data))
