class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        l = len(s)
        if not wordDict:
            return not s
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
test = Solution()
print(test.wordBreak(s, wordDict))
