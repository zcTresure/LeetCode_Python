# File Name:  1443. 收集树上所有苹果的最少时间
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:  # 邻接表 + BFS 求每个节点的直系parent
        grapth = [[] for _ in range(n)]
        parent = [0] * n  # 下标为孩子节点，值为父节点，记录树
        for u, v in edges:
            grapth[u].append(v)
            grapth[v].append(u)
        visited = set()
        visited.add(0)
        stack = [0]
        while stack:
            cur = stack.pop()  # 从根节点开始，保证树的结构
            for son in grapth[cur]:
                if son not in visited:
                    visited.add(son)
                    parent[son] = cur  # 孩子节点的下标记录父节的值
                    stack.append(son)
        visited.clear()
        res = 0
        for i in range(n - 1, -1, -1):  # 从下往上遍历
            if hasApple[i] == True:
                j = i
                while j != 0 and j not in visited:  # 将树枝一直迭代到根节点出
                    visited.add(j)
                    res += 2  # 摘苹果需要一来一回，所有每次需要加两次
                    j = parent[j]  # 更新父节点的值
        return res


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]

test = Solution()
print(test.minTime(n, edges, hasApple))
