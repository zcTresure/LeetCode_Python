from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p = '*' + p
        # 除去重复字串，如'a', 'a'; 'abc', 'abc'
        lens = defaultdict(lambda: 0)
        count = 1
        for i in range(1, len(p)):
            tmp = ord(p[i]) - ord(p[i - 1])
            if tmp == 1 or tmp == -25:
                count += 1
            else:
                count = 1
            lens[p[i]] = max(lens[p[i]], count)
        return sum(lens.values())


p = "zabzabc"
test = Solution()
print(test.findSubstringInWraproundString(p))
