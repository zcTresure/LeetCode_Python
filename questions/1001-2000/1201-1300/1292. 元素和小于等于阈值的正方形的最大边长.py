# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
#
# 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。

class Solution:
    # 数组前缀和
    def maxSideLength(self, mat: list, threshold: int) -> list:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x1: int, x2: int, y1: int, y2: int):
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            find = any(get(i, i + mid - 1, j, j + mid - 1) <= threshold for i in range(1, m - mid + 2) for j in
                       range(1, n - mid + 2))
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans


mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
threshold = 4
test = Solution()
print(test.maxSideLength(mat, threshold))
