class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, prices[i] + hold - fee)
            hold = max(hold, cash - prices[i])
        return cash


prices = [1, 3, 2, 8, 4, 9]
fee = 2
test = Solution()
print(test.maxProfit(prices, fee))
