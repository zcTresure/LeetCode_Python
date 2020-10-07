import collections
import heapq


# Hierholzer 算法
# 题目必然存在一条有效路径(至少是半欧拉图)，所以算法不需要回溯（既加入到结果集里的元素不需要删除）
# 整个图最多存在一个死胡同(出度和入度相差1），且这个死胡同一定是最后一个访问到的，否则无法完成一笔画。
# DFS的调用其实是一个拆边的过程（既每次调用删除一条边），一定是递归到这个死胡同后递归函数开始返回。所以死胡同是第一个加入栈中的元素。
# 最后逆序的输出即可。
class Solution:
    def findItinerary(self, tickets: list) -> list:
        vec = collections.defaultdict(list)
        stack = []
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        def dfs(cur: str):
            while vec[cur]:
                tmp = heapq.heappop(vec[cur])
                dfs(tmp)
            stack.append(cur)
        dfs("JFK")
        return stack[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# out = ["JFK", "MUC", "LHR", "SFO", "SJC"]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# out = ["JFK","ATL","JFK","SFO","ATL","SFO"]
test = Solution()
print(test.findItinerary(tickets))
