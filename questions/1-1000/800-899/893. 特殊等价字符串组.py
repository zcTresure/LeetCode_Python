# -*- coding: utf-8 -*-
# File:      893. 特殊等价字符串组.py
# DATA:      2021/9/10
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        ans = set()
        for word in words:
            count = [0] * 52 # 两倍空间, 存储奇下标[0,26), 偶下标[26,52)
            for i, c in enumerate(word):
                count[ord(c) - ord('a') + 26 * (i % 2)] += 1
            ans.add(tuple(count))
        return len(ans)


words = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
print(Solution().numSpecialEquivGroups(words))
