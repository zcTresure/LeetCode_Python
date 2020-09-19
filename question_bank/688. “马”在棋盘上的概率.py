import collections
import copy
from pprint import pprint


class Solution:
    # 没有限制的深搜，会超出时间限制
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def dfs(r: int, c: int, count: int) -> float:
            if r < 0 or r > N - 1 or c < 0 or c > N - 1:
                return 0
            if count == K:
                return 1
            dd = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                  (1, 2), (1, -2), (-1, 2), (-1, -2)]
            res = 0
            for i, j in dd:
                res += dfs(r + i, c + j, count + 1)
            return res / 8
        return dfs(r, c, 0)

    # 动态规划，dp数组记录每个位置的概率最后求和
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dd = [(2, 1), (2, -1), (-2, 1), (-2, -1),
              (1, 2), (1, -2), (-1, 2), (-1, -2)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for i in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in dd:
                        curr, curc = r + dr, c + dc
                        if 0 <= curr < N and 0 <= curc < N:
                            dp2[curr][curc] += val / 8.0
            dp = dp2
        return sum(map(sum, dp))

    # 动态规划化简版
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        p = {(r, c): 1}
        for _ in range(K):
            p = {(r, c): sum(p.get((r + i, c + j), 0) + p.get((r + j, c + i), 0) for i in (1, -1) for j in (2, -2)) / 8
                 for r in range(N) for c in range(N)}
        return sum(p.values())

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # 最简单的想法，就是用dfs把所有的可能遍历完，然后统计不出界的数目，最后除以8**K
        # 其次的想法，我认为有一些行为是完全对称的，应该是可以避免重复计算的。
        vis = collections.defaultdict(int)

        def dfs(N, K, i, j):
            if not (0 <= i < N and 0 <= j < N):  # 出界
                return 0
            if K == 0:  # 用完步数
                return 1
            cur_cnt = 0
            for d_i, d_j in zip([-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]):
                next_i, next_j = i + d_i, j + d_j
                if not vis[(K - 1, next_i, next_j)]:
                    temp = dfs(N, K - 1, next_i, next_j)
                    cur_cnt += temp
                    vis[(K - 1, next_i, next_j)] = temp
                else:
                    cur_cnt += vis[(K - 1, next_i, next_j)]
            return cur_cnt
        return dfs(N, K, r, c) / 8**K

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = list()
        for i in range(N):
            dp.append([0] * N)
        dp[r][c] = 1
        for k in range(K):
            tmp = copy.deepcopy(dp)
            for i in range(N):
                for j in range(N):
                    d1 = tmp[i - 1][j - 2] if i > 0 and j > 1 else 0
                    d2 = tmp[i - 1][j + 2] if i > 0 and j < N - 2 else 0
                    d3 = tmp[i + 1][j - 2] if i < N - 1 and j > 1 else 0
                    d4 = tmp[i + 1][j + 2] if i < N - 1 and j < N - 2 else 0
                    d5 = tmp[i - 2][j - 1] if i > 1 and j > 0 else 0
                    d6 = tmp[i - 2][j + 1] if i > 1 and j < N - 1 else 0
                    d7 = tmp[i + 2][j - 1] if i < N - 2 and j > 0 else 0
                    d8 = tmp[i + 2][j + 1] if i < N - 2 and j < N - 1 else 0
                    dp[i][j] = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8) / 8
        ret = 0.0
        for i in range(N):
            for j in range(N):
                ret += dp[i][j]
        return ret


N, K, r, c = 3, 2, 0, 0
test = Solution()
print(test.knightProbability(N, K, r, c))
