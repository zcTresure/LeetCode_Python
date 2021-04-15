class Solution:
    def videoStitching(self, clips: list, T: int) -> int:
        dp = [0] + [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        return -1 if dp[T] == float('inf') else dp[T]

    def videoStitching(self, clips: list, T: int) -> int:
        maxLen = [0] * T
        for start, end in clips:
            if start < T:
                maxLen[start] = max(maxLen[start], end)
        last = res = pre = 0
        for i in range(T):
            last = max(maxLen[i], last)
            if i == last:
                return -1
            if i == pre:
                res += 1
                pre = last
        return res


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10
test = Solution()
print(test.videoStitching(clips, T))
