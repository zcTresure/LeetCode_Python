class Solution:
    def transpose(self, A: list) -> list:
        m, n = len(A), len(A[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = A[i][j]
        return ans


A = [[1, 2, 3], [4, 5, 6]]
test = Solution()
print(test.transpose(A))
