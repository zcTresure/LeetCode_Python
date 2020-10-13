from typing import List


class Solution:
    # 二维前缀和
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        tmp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tmp[i][j] = tmp[i - 1][j] + tmp[i][j - 1] - tmp[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x: int, y: int) -> int:
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return tmp[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K,
                                                                                                            j - K);
        return ans

    # 卷积
    def matrixBlockSum(self, mat: list, K: int) -> list:
        def convolution(mat: List[List[int]], K: int):
            m, n = len(mat), len(mat[0])
            ans = [[0] * n for _ in range(m)]
            for i in range(m):
                ans[i][0] = sum(mat[i][:K + 1])
                for j in range(1, n):
                    if j + K < n:
                        ans[i][j] = ans[i][j - 1] + mat[i][j + K]
                    else:
                        ans[i][j] = ans[i][j - 1]
                    if j - K - 1 >= 0:
                        ans[i][j] -= mat[i][j - K - 1]
            return ans

        return list(zip(*convolution(list(zip(*convolution(mat, K))), K)))


mat = [[0, 0, 0, 0], [0, 67, 131, 209], [0, 166, 328, 444], [0, 248, 456, 618], [0, 254, 514, 731], [0, 309, 668, 930]]
K = 1
test = Solution()
ans = test.matrixBlockSum(mat, K)
for i in range(len(ans)):
    print(ans[i])
