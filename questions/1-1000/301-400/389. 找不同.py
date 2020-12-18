# Date:       2020/12/18
# Coding:      UTF-8
__author__ = "zcTresure"

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = [0] * 26
        countT = [0] * 26
        for c in s:
            countS[ord(c) - ord('a')] += 1
        for c in t:
            countT[ord(c) - ord('a')] += 1
        for i in range(26):
            if countS[i] != countT[i]:
                return chr(97 + i)
        return ""


s = ""
t = "y"
test = Solution()
print(test.findTheDifference(s, t))
