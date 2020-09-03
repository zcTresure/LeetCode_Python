class Solution:
    # 递归 总分大于零 则先手获胜 反之 后手获胜
    def PredictTheWinner(self, nums: list) -> bool:
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            sorceStart = nums[start] * turn + total(start + 1, end, -turn)
            sorceEnd = nums[end] * turn + total(start, end - 1, -turn)
            return max(sorceStart * turn, sorceEnd * turn) * turn
        return total(0, len(nums) - 1, 1) >= 0

    # 动态规划 二维数组
    def PredictTheWinner(self, nums: list) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(n - 2, - 1, - 1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

    # 动态规划 空间优化 一维数组
    def PredictTheWinner(self, nums: list) -> bool:
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(n - 2, - 1, - 1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[n - 1] >= 0


# nums = [1, 5, 2]
nums = [1, 5, 233, 7]
test = Solution()
print(test.PredictTheWinner(nums))
