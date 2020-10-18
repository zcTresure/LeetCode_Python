class Solution:
    # 暴力，时间超限
    def maxProfit(self, prices: list) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans

    # 一次遍历，查找前面最小的和最大的差值
    def maxProfit(self, prices: list) -> int:
        res, buy = 0, float("inf")
        for price in prices:
            buy = min(price, buy)
            res = max(res, price - buy)
        return res


prices = [7, 6, 1, 2, 6, 4, 6, 7]
test = Solution()
print(test.maxProfit(prices))
