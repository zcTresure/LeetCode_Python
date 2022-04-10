# -*- coding: utf-8 -*-
# File:      804. 唯一摩尔斯密码词.py
# DATA:      2022/4/10
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        return len(set("".join(Morse[ord(ch) - ord('a')] for ch in word) for word in words))


words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))
