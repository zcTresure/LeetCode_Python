class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                ans += 1
        return ans


s = "RLRRLLRLRL"
test = Solution()
print(test.balancedStringSplit(s))
