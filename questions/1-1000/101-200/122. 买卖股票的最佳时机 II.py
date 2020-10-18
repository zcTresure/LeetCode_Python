class Solution:
    # 峰谷法
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        buy, sell, i, res = float("inf"), 0, 0, 0
        while i < n:
            while i < n and prices[i] <= buy:
                buy = prices[i]
                i += 1
            while i < n and prices[i] >= sell:
                sell = prices[i]
                i += 1
            res += (sell - buy) if sell > buy else 0
            buy, sell = float("inf"), 0
        return res

    # 一次遍历
    def maxProfit(self, prices: list) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


prices = [1, 2, 3, 4, 5]
test = Solution()
print(test.maxProfit(prices))
