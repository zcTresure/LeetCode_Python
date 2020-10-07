class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        def match(words: str) -> bool:
            m1, m2 = {}, {}
            for w, p in zip(words, pattern):
                # 存储words -> pattern 的映射
                if w not in m1:
                    m1[w] = p
                # 存储pattern -> words 的映射
                if p not in m2:
                    m2[p] = w
                # 当前两个字符与映射不同时 匹配失败
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        return list(filter(match, words))


words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(Solution().findAndReplacePattern(words, pattern))
