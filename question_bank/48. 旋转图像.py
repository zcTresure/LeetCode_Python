class Solution:
    def rotate(self, matrix: list) -> None:
        pos1, pos2 = 0, len(matrix) - 1
        while pos1 < pos2:
            add = 0
            while add < pos2 - pos1:
                temp = matrix[pos2 - add][pos1]
                matrix[pos2 - add][pos1] = matrix[pos2][pos2 - add]
                matrix[pos2][pos2 - add] = matrix[pos1 + add][pos2]
                matrix[pos1 + add][pos2] = matrix[pos1][pos1 + add]
                matrix[pos1][pos1 + add] = temp
                add = add + 1
            pos1 = pos1 + 1
            pos2 = pos2 - 1

    def rotate(self, matrix: list) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            matrix[i].reverse()


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
test = Solution()
test.rotate(matrix)
for i in range(len(matrix)):
    print(matrix[i])
