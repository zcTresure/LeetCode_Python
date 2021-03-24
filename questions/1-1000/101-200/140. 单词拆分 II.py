

__author__ = "zcTresure"

from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        @lru_cache(None)
        def backtrack(index: int) -> list:
            if index == n:
                return [[]]
            ans = list()
            for i in range(index + 1, n + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        n = len(s)
        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
test = Solution()
print(test.wordBreak(s, wordDict))
