class Solution:
    def lu_decomp(self, matrix: list) -> None:
        rows, columns = len(matrix), len(matrix[0])
        s = min(rows, columns)
        for i in range(s):
            if matrix[i][i]:
                x = 1.0 / matrix[i][i]
                for j in range(i + 1, rows):
                    matrix[j][i] = matrix[j][i] * x
                for j in range(i + 1, rows):
                    for k in range(i + 1, columns):
                        matrix[j][k] = matrix[j][k] - \
                            matrix[j][i] * matrix[i][k]
            else:
                pass


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
test = Solution()
test.lu_decomp(matrix)
for i in range(len(matrix)):
    print(matrix[i])
