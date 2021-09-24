# -*- coding: utf-8 -*-
# File:      472. 连接词.py
# DATA:      2021/9/23
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = list()
        trie = {}
        for word in words:
            if not word: continue
            curr = trie
            for ch in word:
                curr = curr.setdefault(ch, {})
            curr['#'] = '#'

        def dfs(word: str, index: int, num: int, curr: {}):
            if index == len(word):
                return num > 0 and '#' in curr
            if '#' in curr:
                if dfs(word, index, num + 1, trie):
                    return True
            if word[index] not in curr:
                return False
            if dfs(word, index + 1, num, curr[word[index]]):
                return True
            return False

        for word in words:
            if (dfs, 0, 0, trie):
                ans.append(word)
        return ans

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        min_len = max(1, len(words[0]))
        prev = set()
        res = []

        # 方法1 动态规划方法判断
        # def check(word, prev):
        #     if not prev: return False
        #     n = len(word)
        #     dp = [False] * (n + 1)
        #     dp[0] = True
        #     for i in range(1, n + 1):
        #         for j in range(i):
        #             if not dp[j]: continue
        #             if word[j:i] in prev:
        #                 dp[i] = True
        #                 break
        #     return dp[-1]

        # 方法2, DFS吧
        # def check(word):
        #     if not prev: return False
        #     if not word: return True
        #     for i in range(1, len(word) + 1):
        #         if word[:i] in prev and check(word[i:]):
        #             return True
        #     return False

        # 方法3, 加了一个长度限制, 速度加快很多
        def check(word):
            if word in prev: return True
            for i in range(min_len, len(word) - min_len + 1):
                if word[:i] in prev and check(word[i:]):
                    return True
            return False

        for word in words:
            if check(word):
                res.append(word)
            prev.add(word)
        return res


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(Solution().findAllConcatenatedWordsInADict(words))
