class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        n = len(A)
        top1, ans = A[0], 0
        for i in range(1, n):
            ans = max(ans, top1 + A[i] - i)
            top1 = max(top1, A[i] + i)
        return ans


A = [8, 1, 5, 2, 6]
test = Solution()
print(test.maxScoreSightseeingPair(A))
