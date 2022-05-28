from collections import defaultdict


class Solution:
    # 动态规划
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        count = 0
        for i, ch in enumerate(p):
            if count > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:
                count += 1
            else:
                count = 1
            dp[ch] = max(dp[ch], count)
        return sum(dp.values())

    def findSubstringInWraproundString(self, p: str) -> int:
        p = '*' + p
        lens = defaultdict(int)
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
