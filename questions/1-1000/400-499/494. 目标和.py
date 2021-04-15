class Solution:
    def findTargetSumWays(self, nums: list, S: int) -> int:
        def calculate(i: int, sums: int):
            nonlocal res
            if i == len(nums):
                if sums == S:
                    res += 1
                    return
            else:
                calculate(i + 1, sums + nums[i])
                calculate(i + 1, sums - nums[i])

        res = 0
        calculate(0, 0)
        return res

    def findTargetSumWays(self, nums: list, S: int) -> int:
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, n):
            for j in range(-1000, 1001):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + 1000 + nums[i]] += dp[i - 1][j + 1000]
                    dp[i][j + 1000 - nums[i]] += dp[i - 1][j + 1000]

        return 0 if S > 1000 else dp[n - 1][S + 1000]

    # 01背包
    def findTargetSumWays(self, nums: list, S: int) -> int:
        sumN = sum(nums)
        if sumN < S or sumN + S & 1:
            return 0
        P = (sumN + S) // 2
        dp = [1] + [0 for i in range(P)]
        print(dp)
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
                print(dp)
        return dp[P]

    # 动态规划
    def findTargetSumWays(self, nums: list, S: int) -> int:
        length, dp = len(nums), {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


nums = [1, 1, 1, 1, 1]
S = 3
test = Solution()
print(test.findTargetSumWays(nums, S))
