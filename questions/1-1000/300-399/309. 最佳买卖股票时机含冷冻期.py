class Solution:
    # 递归
    def maxProfit(self, prices: list) -> int:
        n = len(prices)

        def dfs(index, status):
            if index >= n:
                return 0
            # 定义三个变量，分别记录[不动]、[买]、[卖]
            a, b, c = 0, 0, 0
            a = dfs(index + 1, status)
            if status:
                # 递归处理卖的情况
                b = dfs(index + 2, 0) + prices[index]
            else:
                # 递归处理买的情况
                c = dfs(index + 1, 1) - prices[index]
            # 最终结果就是三个变量中的最大值
            return max(a, b, c)

        return dfs(0, 0)

    # 递归 + 记忆化
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        d = dict()

        def dfs(index, status):
            if (index, status) in d:
                return d[index, status]
            if index >= n:
                return 0
            a, b, c = 0, 0, 0
            a = dfs(index + 1, status)
            if status:
                b = dfs(index + 2, 0) + prices[index]
            else:
                c = dfs(index + 1, 1) - prices[index]
            d[index, status] = max(a, b, c)
            return d[index, status]

        return dfs(0, 0)

    # 动态规划
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        # 初始化第一天和第二天
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, n):
            # 求第i天累计卖出最大利润，累计买入的最大利润
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return max(dp[-1][0], dp[-1][1])

    # 动态规划
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        # 初始化第一天(卖出、买入、冷冻期)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            # 求第i天累计卖出最大利润，累计买入的最大利润、冷冻期内最大利润
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
            dp[i][2] = dp[i - 1][0]
        return max(dp[-1][0], dp[-1][1], dp[-1][2])

    # 动态规划 + 空间优化
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # 初始化第一天
        dp0 = 0
        dp1 = -prices[0]
        dp2 = 0
        for i in range(1, n):
            # 这里的dp0相当于二维数组的dp[i][0] 卖出收益
            # dp1相当于dp[i][1] 买入收益
            # dp2相当于dp[i][2] 冷冻期内的收益
            tmp = dp0
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp2 - prices[i])
            dp2 = tmp
        return max(dp0, dp1, dp2)


prices = [1, 2, 3, 0, 2]
test = Solution()
print(test.maxProfit(prices))
