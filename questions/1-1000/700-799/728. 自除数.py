# -*- coding: utf-8 -*-
# File:      728. 自除数.py
# DATA:      2022/3/31
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            tmp = i
            flag = True
            while tmp:
                digit = tmp % 10
                tmp //= 10
                if digit == 0 or i % digit != 0:
                    flag = False
                    break
            if flag:
                ans.append(i)
        return ans


print(Solution().selfDividingNumbers(left=1, right=22))
print(Solution().selfDividingNumbers(left=47, right=85))
