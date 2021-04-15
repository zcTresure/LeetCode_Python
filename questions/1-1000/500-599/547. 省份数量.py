# Date:       2021/1/8
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles


test = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(test.findCircleNum(isConnected))
