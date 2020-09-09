class Solution:
    def setZeroes(self, matrix: list) -> None:
        n, m = len(matrix), len(matrix[0])
        row = set()
        column = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(m):
                matrix[i][j] = 0
        for j in column:
            for i in range(n):
                matrix[i][j] = 0


matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
test = Solution()
test.setZeroes(matrix)
for i in range(len(matrix)):
    print(matrix[i])

