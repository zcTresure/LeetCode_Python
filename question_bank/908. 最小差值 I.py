class Solution:
    def smallestRangeI(self, A: list, K: int) -> int:
        return max(0, max(A) - min(A) - 2 * K)


A = [1, 3, 6]
K = 3
test = Solution()
print(test.smallestRangeI(A, K))
