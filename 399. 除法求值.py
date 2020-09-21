from collections import defaultdict, namedtuple, deque


class Item():
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value


class Solution:
    # 并查集
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        # 查找X的根节点
        def find(x: str) -> str:
            if x != father[x].parent:
                t = father[x].parent
                father[x].parent = find(t)
                #记录根节点到当前节点的权重
                father[x].value *= father[t].value
                return father[x].parent
            # x是单独的一个节点
            return x

        # 合并两棵树
        def union(e1: str, e2: str, result: float):
            f1 = find(e1)
            f2 = find(e2)
            if f1 != f2:
                father[f1].parent = f2
                # (1 -> 3) = (1 -> 2) * (2 -> 3)
                father[f1].value = father[e2].value * result / father[e1].value

        number = defaultdict(int)
        father = defaultdict(Item)
        for i, item in enumerate(equations):
            s1, s2 = item[0], item[1]
            if s1 not in number:
                number[s1] = 1
                father[s1] = Item(parent=s1, value=1)
            if s2 not in number:
                number[s2] = 1
                father[s2] = Item(parent=s2, value=1)
            union(s1, s2, values[i])
        res = []
        for s1, s2 in queries:
            if s1 not in number or s2 not in number:
                res.append(-1.0)
                continue
            f1, f2 = find(s1), find(s2)
            if f1 != f2:
                res.append(-1.0)
            else:
                res.append(father[s1].value / father[s2].value)
        return res

    # 深度优先搜索
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        # 建立图
        graph = defaultdict(set)
        weight = defaultdict()
        for index, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            # 记录每条边上赋权值
            weight[tuple(equ)] = values[index]
            # 记录反向边赋权值的倒数
            weight[(equ[1], equ[0])] = float(1 / values[index])

        def dfs(start, end, visited):
            # (start, end)被记录过直接返回权值
            if (start, end) in weight:
                return weight[(start, end)]
            # 边在图上或者边已近被访问过了 则直接退出
            if start not in graph or end not in graph or start in visited:
                return 0
            # 没访问过的节点加入集合中
            visited.add(start)
            res = 0
            for tmp in graph[start]:
                # 对相邻的边权值求积
                res = (dfs(tmp, end, visited) * weight[(start, tmp)])
                if res != 0:
                    weight[(start, end)] = res
                    break
            # 移除当前节点 访问前驱节点的下一条边
            visited.remove(start)
            return res
        res = []
        for que in queries:
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res

    # 广度优先搜索
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        graph = defaultdict(set)
        weight = defaultdict()
        for index, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[index]
            weight[(equ[1], equ[0])] = float(1 / values[index])
        res = []
        for start, end in queries:
            if (start, end) in weight:
                res.append(weight[(start, end)])
                continue
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            if start == end:
                res.append(1)
                continue
            stack = deque()
            for tmp in graph[start]:
                stack.appendleft((tmp, weight[(start, tmp)]))
            visited = set(stack)
            flag = False
            while stack:
                c, w = stack.pop()
                if c == end:
                    flag = True
                    res.append(w)
                    break
                visited.add(c)
                for n in graph[c]:
                    if n not in visited:
                        weight[(start, n)] = w * weight[(c, n)]
                        stack.appendleft((n, w * weight[(c, n)]))
            if flag:
                continue
            res.append(-1)
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
test = Solution()
print(test.calcEquation(equations, values, queries))
