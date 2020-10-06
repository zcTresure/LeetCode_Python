class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n // 2):
                A[i][j], A[i][n - j - 1] = A[i][n - j - 1], A[i][j]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A


A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
test = Solution()
print(test.flipAndInvertImage(A))
