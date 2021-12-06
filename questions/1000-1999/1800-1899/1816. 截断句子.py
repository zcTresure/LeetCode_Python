# -*- coding: utf-8 -*-
# File:      1816. 截断句子.py
# DATA:      2021/12/6
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        n = len(s)
        end, cnt = 0, 0
        for i in range(1, n + 1):
            if i == n or s[i] == ' ':
                cnt += 1
                if cnt == k:
                    end = i
                    break
        return s[:end]

    def truncateSentence(self, s: str, k: int) -> str:
        tmp = s.split()
        return " ".join(tmp[x] for x in range(len(tmp)) if x < k)


s = "Hello how are you Contestant"
k = 4
print(Solution().truncateSentence(s, k))
