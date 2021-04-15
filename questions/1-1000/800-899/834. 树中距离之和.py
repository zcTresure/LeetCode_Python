class Solution:
    def sumOfDistancesInTree(self, N: int, edges: list) -> list:
        tree = [[] for _ in range(N)]
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        level = [0] * N
        nextCount = [0] * N

        def dfsForDepthAndNextCount(node1: int, node2: int) -> None:
            nextCount[node1] = 1
            for son in tree[node1]:
                if son != node2:
                    level[son] = level[node1] + 1
                    dfsForDepthAndNextCount(son, node1)
                    nextCount[node1] += nextCount[son]

        dfsForDepthAndNextCount(0, -1)
        ans = [0] * N
        ans[0] = sum(level)

        def dfsForAns(node1: int, node2: int) -> None:
            for son in tree[node1]:
                if son != node2:
                    ans[son] = ans[node1] + N - 2 * nextCount[son]
                    dfsForAns(son, node1)

        dfsForAns(0, -1)
        return ans

    # 树形dp
    def sumOfDistancesInTree(self, N: int, edges: list) -> list:
        ans = [0] * N
        size = [0] * N
        dp = [0] * N
        graph = [[] for _ in range(N)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs1(u, f):
            size[u], dp[u] = 1, 0
            for v in graph[u]:
                if v == f:
                    continue
                dfs1(v, u)
                dp[u] += dp[v] + size[v]
                size[u] += size[v]

        def dfs2(u, f):
            ans[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue
                pu, pv, su, sv = dp[u], dp[v], size[u], size[v]
                dp[u] -= dp[v] + size[v]
                size[u] -= size[v]
                dp[v] += dp[u] + size[u]
                size[v] += size[u]
                dfs2(v, u)
                dp[u], dp[v], size[u], size[v] = pu, pv, su, sv

        dfs1(0, -1)
        dfs2(0, -1)
        return ans


N = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
test = Solution()
print(test.sumOfDistancesInTree(N, edges))
