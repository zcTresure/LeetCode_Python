class Solution:
    # 递归
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0

        def dfs(index: int, status: int, k: int) -> int:
            # 终止条件：数组遍历完或买卖两次
            if index == n or k == 2:
                return 0
            # 三个变量记录 保持不动、买入、卖出 三种状态
            keep = buy = sell = 0
            # 保持不动
            keep = dfs(index + 1, status, k)
            if status:
                # 买入
                buy = dfs(index + 1, 0, k + 1) + prices[index]
            else:
                # 卖出
                sell = dfs(index + 1, 1, k) - prices[index]
            return max(keep, buy, sell)

        return dfs(0, 0, 0)

    # 递归 + 记忆化
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        d = dict()

        def dfs(index: int, status: int, k: int) -> int:
            if (index, status, k) in d:
                return d[index, status, k]
            if index == n or k == 2:
                return 0
            keep = buy = sell = 0
            keep = dfs(index + 1, status, k)
            if status:
                buy = dfs(index + 1, 0, k + 1) + prices[index]
            else:
                sell = dfs(index + 1, 1, k) - prices[index]
            d[index, status, k] = max(keep, buy, sell)
            return d[index, status, k]

        return dfs(0, 0, 0)

    # 动态规划 三维数组
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # 定义三维数组，第i天、交易了多少次、当前的买卖状态
        dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]

        dp[0][0][0] = dp[0][1][0] = dp[0][2][0] = 0
        dp[0][0][1] = dp[0][1][1] = dp[0][2][1] = -prices[0]
        for i in range(1, n):
            dp[i][0][0] = -dp[i - 1][0][0]
            # 第一次买卖
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
            # 第二次买卖
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])
        return max(dp[-1][0][0], dp[-1][0][1], dp[-1][1][0], dp[-1][1][1], dp[-1][2][0])

    # 动态规划
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n < 2:
            return 0
        # 定义二维数组，5种状态
        dp = [[-1 for _ in range(5)] for _ in range(n)]
        # 初始化第一天的状态
        dp[0][0] = dp[0][2] = dp[0][4] = 0
        dp[0][1] = dp[0][3] = -prices[0]

        for i in range(1, n):
            # dp[i][0]相当于初始状态，它只能从初始状态转换来
            dp[i][0] = 0
            # 处理第一次买入、第一次卖出
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            # 处理第二次买入、第二次卖出
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # 返回最大值
        return max(dp[-1][0], dp[-1][1], dp[-1][2], dp[-1][3], dp[-1][4])

    # 动态规划 空间优化
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 定义5种状态，并初始化第一天的状态
        dp0 = dp2 = dp4 = 0
        dp1 = dp3 = -prices[0]
        for i in range(1, n):
            # 这里省略dp0，因为dp0每次都是从上一个dp0来的相当于每次都是0
            # 处理第一次买入、第一次卖出
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
            # 处理第二次买入、第二次卖出
            dp3 = max(dp3, dp2 - prices[i])
            dp4 = max(dp4, dp3 + prices[i])
        # 返回最大值
        return max(dp0, dp1, dp2, dp3, dp4)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
test = Solution()
print(test.maxProfit(prices))
