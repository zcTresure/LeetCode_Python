class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        if not timeSeries:
            return 0
        ans = duration
        for i in range(1, len(timeSeries)):
            ans += min(timeSeries[i] - timeSeries[i - 1], duration)
        return ans


timeSeries = [1, 2]
duration = 2
test = Solution()
print(test.findPoisonedDuration(timeSeries, duration))
