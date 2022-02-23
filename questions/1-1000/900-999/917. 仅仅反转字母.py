# -*- coding: utf-8 -*-
# File:      917. 仅仅反转字母.py
# DATA:      2022/2/23
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left, right = 0, len(ans) - 1
        while left < right:
            while left < right and not ans[left].isalpha():
                left += 1
            while left < right and not ans[right].isalpha():
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1

        return "".join(ans)


print(Solution().reverseOnlyLetters(s='ab-cd'))
