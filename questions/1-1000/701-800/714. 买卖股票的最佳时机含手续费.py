class Solution:
    # 一次遍历
    def maxProfit(self, prices: list, fee: int) -> int:
        res, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] + hold - fee)
            hold = max(hold, res - prices[i])
        return res

    # 递归
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        n = len(prices)

        def dfs(index, status):
            if index == n:
                return 0
            # 定义三个变量，分别记录[不动]、[买]、[卖]
            a = dfs(index + 1, status)
            b, c = 0, 0
            if status:
                # 递归处理卖的情况，卖的时候会有一个手续费
                b = dfs(index + 1, 0) + prices[index] - fee
            else:
                # 递归处理买的情况
                c = dfs(index + 1, 1) - prices[index]
            # 最终结果就是三个变量中的最大值
            return max(a, b, c)

        return dfs(0, 0)

    # 递归 + 记忆化
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        n = len(prices)
        d = dict()
        def dfs(index,status):
            if (index,status) in d:
                return d[index,status]
            if index==n:
                return 0
            a,b,c = 0,0,0
            a = dfs(index+1,status)
            if status:
                b = dfs(index+1,0)+prices[index]-fee
            else:
                c = dfs(index+1,1)-prices[index]
            d[index,status] = max(a,b,c)
            return d[index,status]
        return dfs(0,0)

prices = [1, 3, 2, 8, 4, 9]
fee = 2
test = Solution()
print(test.maxProfit(prices, fee))
