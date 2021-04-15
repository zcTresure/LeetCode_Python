# File Name:  1766. 互质树
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import defaultdict
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # 最大公约数
        def gcd(a, b):
            return gcd(b, a % b) if b else a

        # 构建无向图邻接表
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # 预处理[1,50]中互质的数据对
        prime = defaultdict(set)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    prime[i].add(j)
                    prime[j].add(i)

        # 深度优先搜索
        def dfs(root):
            index = -1
            for u in prime[nums[root]]:
                index = max(index, depth[u])
            res[root] = -1 if index == -1 else stack[index]
            tmp = depth[nums[root]]
            depth[nums[root]] = len(stack)
            stack.append(root)
            visited.add(root)
            for nex in graph[root]:
                if nex not in visited:
                    dfs(nex)

            depth[nums[root]] = tmp
            stack.pop()

        n = len(nums)
        visited = set()
        depth = [-1] * 51
        res = [-1] * n
        stack = []
        dfs(0)
        return res


nums = [2, 3, 3, 2]
edges = [[0, 1], [1, 2], [1, 3]]
test = Solution()
print(test.getCoprimes(nums, edges))
