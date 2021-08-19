# -*- coding: utf-8 -*-
# File:      345. 反转字符串中的元音字母.py
# DATA:      2021/8/19
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_dict = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        list_s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and list_s[i] not in vowel_dict:
                i += 1
            while j > 0 and list_s[j] not in vowel_dict:
                j -= 1
            if i < j:
                list_s[i], list_s[j] = list_s[j], list_s[i]
                i += 1
                j -= 1
        return "".join(list_s)


# s = 'hello'
s = 'HELLo'
print(Solution().reverseVowels(s))
