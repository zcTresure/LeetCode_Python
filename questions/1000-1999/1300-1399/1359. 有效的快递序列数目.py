class Solution:
    def countOrders(self, n: int) -> int:
        ans, tmp = 1, 1
        for i in range(2, n + 1):
            ans = (i * 2 - 1) * i * ans % 1000000007
        return ans


test = Solution()
print(test.countOrders(3))
