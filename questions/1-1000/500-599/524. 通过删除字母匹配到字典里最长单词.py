# -*- coding: utf-8 -*-
# File:      524. 通过删除字母匹配到字典里最长单词.py
# DATA:      2021/9/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 双指针
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                return word
        return ""

    # 动态规划
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        m = len(s)
        dp = [[0] * 26 for _ in range(m)]
        dp.append([m] * 26)
        for i in range(m - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(s[i]) == 97 + j else dp[i + 1][j]
        ans = ""
        for word in dictionary:
            j, match = 0, True
            for i in range(len(word)):
                if dp[j][ord(word[i]) - 97] == m:
                    match = False
                    break
                j = dp[j][ord(word[i]) - 97] + 1
            if match:
                if len(word) > len(ans) or (len(word) == len(ans) and ans > word):
                    ans = word
        return ans


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
print(Solution().findLongestWord(s, dictionary))
