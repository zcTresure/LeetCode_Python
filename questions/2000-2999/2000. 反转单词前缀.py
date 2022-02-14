# -*- coding: utf-8 -*-
# File:    2000. 反转单词前缀.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch) + 1
        return word[:index][::-1] + word[index:]


print(Solution().reversePrefix(word="abcdefg", ch="d"))
