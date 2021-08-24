from typing import List
from collections import defaultdict
import heapq


class Solution:
    # 计算到各节点的最短距离
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [[float("inf")] * n for _ in range(2)]
        dist[0][src] = dist[1][src] = 0
        for i in range(K + 1):
            for u, v, w in flights:
                dist[i & 1][v] = min(dist[i & 1][v], dist[~i & 1][u] + w)
        return dist[K & 1][dst] if dist[K & 1][dst] else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        ans = float("inf")
        for i in range(1, k + 2):
            go = [float('inf')] * n
            for f, t, c in flights:
                go[t] = min(go[t], dist[f] + c)
            dist = go
            ans = min(ans, dist[dst])
        return -1 if ans == float('inf') else ans

    # Dijkstra
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K + 1 or cost > best.get((k, place), float("inf")):
                continue
            if place == dst:
                return cost
            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best.get((k + 1, nei), float("inf")):
                    heapq.heappush(pq, (newcost, k + 1, nei))
                    best[k + 1, nei] = newcost
        return -1


n = 5
flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
src, dst, k = 2, 1, 1
test = Solution()
print(test.findCheapestPrice(n, flights, src, dst, k))
