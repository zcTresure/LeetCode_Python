class Solution:
    def rotate(self, matrix: list) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                k = n - 1 - j
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
        return matrix

    def rotate(self, matrix: list) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]
        return matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
test = Solution()
matrix = test.rotate(matrix)
for i in range(len(matrix)):
    print(matrix[i])
