class Solution:
    def binaryGap(self, N: int) -> int:
        ans, last = 0, None
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i

        return ans


test = Solution()
print(test.binaryGap(22))
