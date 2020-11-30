# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        finalStack = numStack[:-k] if k else numStack
        return "".join(finalStack).lstrip('0') or "0"


num = "1432219"
k = 3
test = Solution()
print(test.removeKdigits(num, k))
