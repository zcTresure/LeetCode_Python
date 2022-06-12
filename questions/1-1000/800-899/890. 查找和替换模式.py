from typing import List


class Solution:
    # 单射函数
    def match(self, word: str, pattern: str) -> bool:
        cmp = {}
        for w, p in zip(word, pattern):
            if w not in cmp:
                cmp[w] = p
            elif cmp[w] != p:
                return False
        return True

    # 通过两个单射构建双射
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if self.match(word, pattern) and self.match(pattern, word)]

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(Solution().findAndReplacePattern(words, pattern))
