class Solution:
    def rotate(self, matrix: list) -> None:
        n = len(matrix)
        for i in range(n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for j in range(1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            print(matrix[i])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
test = Solution()
test.rotate(matrix)
