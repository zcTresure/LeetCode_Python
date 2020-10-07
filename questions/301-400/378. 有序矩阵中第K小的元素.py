class Solution:
    # 二维数组转一维数组 排序后直接输出
    def kthSmallest(self, matrix: list, k: int) -> int:
        matrix = list(sorted(chain.from_iterable(matrix)))
        return matrix

    # 直接排序
    def kthSmallest(self, matrix: list, k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]

    # 二分查找
    def kthSmallest(self, matrix: list, k: int) -> int:
        n = len(matrix)

        def check(mid: int):
            i, j, num = n - 1, 0, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
test = Solution()
print(test.kthSmallest(matrix, k))
