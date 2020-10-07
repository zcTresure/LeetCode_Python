class Solution():
    # 计数
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        def count(num):
            ans = cur = 0
            for a in A:
                cur = cur + 1 if a <= num else 0
                ans += cur
            return ans
        return count(R) - count(L - 1)

    # 动态规划
    def numSubarrayBoundedMax(self, A: list, L: int, R: int) -> int:
        ans = dp = 0
        prev = -1
        for i, num in enumerate(A):
            if num < L:
                ans += dp
            elif num > R:
                dp, prev = 0, i
            else:
                dp = i - prev
                ans += dp
        return ans


A = [2, 1, 4, 3]
L = 2
R = 3
test = Solution()
print(test.numSubarrayBoundedMax(A, L, R))
