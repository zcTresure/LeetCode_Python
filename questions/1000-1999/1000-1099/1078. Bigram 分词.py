# -*- coding: utf-8 -*-
# File:    1078. Bigram 分词.py
# Date:    2021/12/26
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = list()
        words = text.split()
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                ans.append(words[i])
        return ans

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[i] for i in range(2, len(words)) if words[i - 2] == first and words[i - 1] == second]


text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(Solution().findOcurrences(text, first, second))
