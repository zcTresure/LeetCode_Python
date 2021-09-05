# -*- coding: utf-8 -*-
# File:      470. 用 Rand7() 实现 Rand10().py
# DATA:      2021/9/5
# Software:  PyCharm
__author__ = 'zcFang'

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random


class Solution:
    def rand7(self) -> int:
        return random.randint(1, 7)

    def rand10(self):
        """
        :rtype: int
        """
        while (True):
            ans = (self.rand7() - 1) * 7 + self.rand7()
            if (ans <= 40):
                return ans % 10 + 1


n = 10
test = Solution()
ans = list()
for _ in range(n):
    ans.append(test.rand10())
print(ans)
