# -*- coding: utf-8 -*-
# File:    306. 累加数.py
# Date:    2022/1/10
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for secondStart in range(1, n - 1):
            if num[0] == '0' and secondStart != 1:
                break
            for secondEnd in range(secondStart, n - 1):
                if num[secondStart] == '0' and secondStart != secondEnd:
                    break
                if self.valid(secondStart, secondEnd, num):
                    return True
        return False

    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        n = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd <= n - 1:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= n or num[thirdStart:thirdEnd + 1] != third:
                break
            if thirdEnd == n - 1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False

    def stringAdd(self, s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third = []
        carry, cur = 0, 0
        while firstEnd >= firstStart or secondEnd >= secondStart or carry != 0:
            cur = carry
            if firstEnd >= firstStart:
                cur += ord(s[firstEnd]) - ord('0')
                firstEnd -= 1
            if secondEnd >= secondStart:
                cur += ord(s[secondEnd]) - ord('0')
                secondEnd -= 1
            carry = cur // 10
            cur %= 10
            third.append(chr(cur + ord('0')))
        return ''.join(third[::-1])


s = "112358"
print(Solution().valid(s))