class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        nodes = len(graph)
        near = [[] for _ in range(nodes)]
        bfs = []
        unsearched = set(list(range(nodes)))
        for i, x in enumerate(graph):
            if len(x) == 0:
                bfs.append(i)
                unsearched.remove(i)
                continue
            for j in graph[i]:
                near[j].append(i)
        res = []
        while bfs:
            x = bfs.pop(0)
            res.append(x)
            for i in near[x]:
                graph[i].remove(x)
                if len(graph[i]) == 0:
                    bfs.append(i)
                    unsearched.remove(i)
        res.sort()

        return res


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
test = Solution()
print(test.eventualSafeNodes((graph)))
