class Solution:
    # 动态规划，用 dp[i] 表示放置前 i 本书所需要的书架最小高度，初始值 dp[0] = 0，其他为最大值 1000*1000。
    # 遍历每一本书，把当前这本书作为书架最后一层的最后一本书，将这本书之前的书向后调整，看看是否可以减少之前的书架高度。
    # 状态转移方程为 dp[i] = min(dp[i] , dp[j - 1] + level_h)，其中 j 表示最后一层所能容下书籍的索引，level_h 表示最后一层最大高度。
    def minHeightShelves(self, books: list, shelf_width: int) -> int:
        n = len(books)
        dp = [0] + [10000000] * n
        for i in range(1, n + 1):
            tmp_width, j, level_h = 0, i, 0
            while j > 0:
                tmp_width += books[j - 1][0]
                # 当前层书的宽度大于书架的宽度提前退出
                if tmp_width > shelf_width:
                    break
                # 更新当前层的宽度
                level_h = max(level_h, books[j - 1][1])
                # 记录书架的总高度
                dp[i] = min(dp[i], dp[j - 1] + level_h)
                j -= 1
        return dp[-1]


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelf_width = 4
test = Solution()
print(test.minHeightShelves(books, shelf_width))
