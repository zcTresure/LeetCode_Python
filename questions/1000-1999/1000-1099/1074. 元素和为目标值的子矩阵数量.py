# Date:       2020/12/25
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import defaultdict, Counter


class Solution:
    # 前缀和
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix[i][j] = matrix[i][j]
                elif i == 0:
                    prefix[i][j] = matrix[i][j] + prefix[i][j - 1]
                elif j == 0:
                    prefix[i][j] = matrix[i][j] + prefix[i - 1][j]
                else:
                    prefix[i][j] = matrix[i][j] + prefix[i - 1][j] + \
                                   prefix[i][j - 1] - prefix[i - 1][j - 1]
                for x in range(i + 1):
                    for y in range(j + 1):
                        a = prefix[x - 1][y - 1] if x and y else 0
                        b = prefix[x - 1][j] if x else 0
                        c = prefix[i][y - 1] if y else 0
                        tmp = prefix[i][j] + a - b - c
                        if tmp == target:
                            ans += 1
        return ans

    # 前缀和+哈希表
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        colms = [[0] * cols for r in range(rows)]  # 存储每一列的前缀和
        for c in range(cols):
            cur = 0
            for r in range(rows):
                cur += matrix[r][c]
                colms[r][c] = cur
        res = 0
        for sr in range(rows):
            for er in range(sr, rows):
                d = defaultdict(int)
                cur = 0
                for c in range(cols):
                    pre = 0 if sr - 1 < 0 else colms[sr - 1][c]  # 注意此处减去的是colms[sr - 1][c], 因为要把起点行sr统计在内
                    cur += colms[er][c] - pre
                    if cur == target:  # cur本身就是target的特殊情况
                        res += 1
                    res += d[cur - target]
                    d[cur] += 1
        return res

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和
                ans += subarraySum(total, target)

        return ans


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 1
test = Solution()
print(test.numSubmatrixSumTarget(matrix, target))
