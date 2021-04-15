class Solution:
    def numSubmat(self, mat: list) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] = 0 if mat[i][j] == 0 else mat[i][j - 1] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                column = mat[i][j]
                for k in range(i, -1, -1):
                    column = min(column, mat[k][j])
                    if column == 0:
                        break
                    ans += column
        return ans


mat = [[1, 0, 1],
       [1, 1, 1],
       [1, 1, 0]]
test = Solution()
print(test.numSubmat(mat))
for i in range(len(mat)):
    print(mat[i])
