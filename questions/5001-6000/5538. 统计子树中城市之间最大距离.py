from collections import defaultdict
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * (n - 1)
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        dis = defaultdict(int)
        # 记录每对节点间的路径长度
        for x in range(1, n + 1):
            visited = set()
            queue = [x]
            path = 0
            while queue:
                path += 1
                for i in range(len(queue)):
                    cur = queue.pop(0)
                    visited.add(cur)
                    for j in dic[cur]:
                        if j not in visited:
                            queue.append(j)
                            dis[(x, j)] = path
        # tmp数组记录状态压缩后每一种子节点集合的情况 ，此处利用位运算进行状态压缩
        for i in range(1, 2 ** n):
            tmp = []
            cur = 0
            while i:
                cur += 1
                if i & 1:# 奇数
                    tmp.append(cur)
                i >>= 1
            if len(tmp) <= 1:
                continue
            road = 0
            # 记录状态压缩后不完全图的边的数量
            for x, y in edges:
                if x in tmp and y in tmp:
                    road += 1
            # 边数不等于节点数-1不满足树的定义
            if road < len(tmp) - 1:
                continue
            maxd = 0
            # 记录最大路径更新结果
            for i in range(len(tmp)):
                for j in range(i + 1, len(tmp)):
                    maxd = max(maxd, dis[tmp[i], tmp[j]])
            res[maxd - 1] += 1
        return res


n = 4
edges = [[1, 2], [2, 3], [2, 4]]
test = Solution()
print(test.countSubgraphsForEachDiameter(n, edges))
