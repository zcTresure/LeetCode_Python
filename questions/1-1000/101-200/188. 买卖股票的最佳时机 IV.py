class Solution:
    # 递归
    def maxProfit(self, k: int, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0

        def dfs(index: int, status: int, count: int) -> int:
            # 终止条件：数组遍历完或买卖两次
            if index == n or k == count:
                return 0
            # 三个变量记录 保持不动、买入、卖出 三种状态
            keep = buy = sell = 0
            # 保持不动
            keep = dfs(index + 1, status, count)
            if status:
                # 买入
                buy = dfs(index + 1, 0, count + 1) + prices[index]
            else:
                # 卖出
                sell = dfs(index + 1, 1, count) - prices[index]
            return max(keep, buy, sell)

        return dfs(0, 0, 0)

    # 递归 + 记忆化
    def maxProfit(self, k: int, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        d = dict()

        def dfs(index: int, status: int, count: int) -> int:
            if (index, status, count) in d:
                return d[index, status, count]
            if index == n or k == count:
                return 0
            keep = buy = sell = 0
            keep = dfs(index + 1, status, count)
            if status:
                buy = dfs(index + 1, 0, count + 1) + prices[index]
            else:
                sell = dfs(index + 1, 1, count) - prices[index]
            d[index, status, count] = max(keep, buy, sell)
            return d[index, status, count]

        return dfs(0, 0, 0)

    # 动态规划
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 当k非常大时转为无限次交易
        if k > n // 2:
            dp0, dp1 = 0, -prices[0]
            for i in range(1, n):
                tmp = dp0
                dp0 = max(dp0, dp1 + prices[i])
                dp1 = max(dp1, tmp - prices[i])
            return max(dp0, dp1)
            # 定义三维数组，第i天、交易了多少次、当前的买卖状态
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        # 初始化第一天，这里的dp[0][k][1]可以不用管，后面也不会用到
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                # 处理第k次买入
                dp[i][j - 1][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0] - prices[i])
                # 处理第k次卖出
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
        return dp[-1][k][0]

    # 动态规划 + 空间优化
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 当k非常大时转为无限次交易
        if k > n // 2:
            dp0, dp1 = 0, -prices[0]
            for i in range(1, n):
                tmp = dp0
                dp0 = max(dp0, dp1 + prices[i])
                dp1 = max(dp1, dp0 - prices[i])
            return max(dp0, dp1)
        # 定义二维数组，交易了多少次、当前的买卖状态
        dp = [[0, 0] for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][1] = -prices[0]
        for i in range(1, n):
            for j in range(k, 0, -1):
                # 处理第k次买入
                dp[j - 1][1] = max(dp[j - 1][1], dp[j - 1][0] - prices[i])
                # 处理第k次卖出
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + prices[i])
        return dp[-1][0]


prices = [3, 2, 6, 5, 0, 3]
k = 2
test = Solution()
print(test.maxProfit(k, prices))
