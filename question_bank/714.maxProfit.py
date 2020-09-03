def maxProfit(self, prices, fee: int):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, prices[i] + hold - fee)
        hold = max(hold, cash - prices[i])
    return cash


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfit(1, prices, fee))
