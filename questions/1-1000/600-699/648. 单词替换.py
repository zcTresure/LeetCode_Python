# -*- coding: utf-8 -*-
# File:      648. 单词替换.py
# DATA:      2021/9/23
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr['#'] = '#'

        def process(word):
            curr = trie
            for i, ch in enumerate(word):
                if ch not in curr:
                    break
                curr = curr[ch]
                if '#' in curr:
                    return word[:i + 1]
            return word

        return ' '.join(map(process, sentence.split()))


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))
