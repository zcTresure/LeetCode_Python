class Solution:
    def smallestRangeII(self, A: list, K: int) -> int:
        A.sort()
        m, n = A[0], A[-1]
        ans = n - m
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(n - K, a + K) - min(m + K, b - K))
        return ans


A = [1, 3, 6]
K = 3
test = Solution()
print(test.smallestRangeII(A, K))
