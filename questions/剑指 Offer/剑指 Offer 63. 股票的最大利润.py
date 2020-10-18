class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices or len(prices) < 2:
            return 0
        res, buy = 0, prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]
        return res


prices = [7, 6]
test = Solution()
print(test.maxProfit(prices))
