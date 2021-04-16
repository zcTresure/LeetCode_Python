# File Name:  1466. 重新规划路线
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connect = [[] for _ in range(n)]
        for i in range(len(connections)):
            connect[connections[i][0]].append(i)
            connect[connections[i][1]].append(i)
        visited = [False] * (n - 1)  # 标志当前边是否被访问过
        ans = 0
        queue = deque([0])
        while queue:
            citys = queue.popleft()
            for city in connect[citys]:  # 对节点city相关的连接进行遍历，通过上面的存储的连接的id进行遍历
                if visited[city]: continue
                visited[city] = True
                a, b = connections[city][0], connections[city][1]  # a:连接的起点 b:连接的终点
                ans += int(a == citys)  # 如果当前节点时出的，则要修改为入，结果加1
                a = b if a == citys else a
                queue.append(a)
        return ans


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
test = Solution()
print(test.minReorder(n, connections))
