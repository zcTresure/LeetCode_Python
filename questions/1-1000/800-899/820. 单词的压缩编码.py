# Date:       2021/3/13
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import defaultdict
from functools import reduce


class Solution:
    def minimumLengthencode(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])  # discard() 方法用于移除指定的集合元素
        return sum(len(word) + 1 for word in good)

    def minimumLengthencode(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda word: word[::-1])
        res = 0
        for i in range(n):
            if i + 1 < n and words[i + 1].endswith(words[i]):
                pass  # endwise()判断字符串是否以指定后缀结尾
            else:
                res += 1 + len(words[i])
        return res


words = ["time", "me", "bell", "meat"]
test = Solution()
print(test.minimumLengthencode(words))
# meatime#bell#
