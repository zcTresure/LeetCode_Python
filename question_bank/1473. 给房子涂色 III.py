class Solution:
    def minCost(self, houses: list, cost: list, m: int, n: int,
                target: int) -> int:
        dp = collections.defaultdict(int)
        res = float('inf')
        for i in range(m):
            # paint表示是否需要涂色
            paint = True
            if houses[i] != 0:
                # colors表示当前可选的颜色
                colors = [houses[i]]
                # 已有颜色, 不需要涂色
                paint = False
            else:
                colors = range(1, n + 1)
            for j in colors:
                # 计算涂成当前颜色时的cost, 注意已有颜色的情况下cost就是0
                curcost = (0 if not paint else cost[i][j - 1])
                ii = i - 1
                if i == 0:
                    # 第0号房子, 前面没有房子, 所以街区数一定为1, 花费也就是curcost
                    dp[i, j, 1] = curcost
                    continue
                for jj in range(1, n + 1):
                    for b in range(i + 1):
                        # 街区数一定不会超过当前的房子数, 因为极限情况也是一个房子一个街区
                        if (ii, jj, b) in dp:
                            # 根据前一个房子的颜色计算当前的街区数
                            if j == jj:
                                newb = b
                            else:
                                newb = b + 1
                            # 更新当前dp值
                            if (i, j, newb) not in dp:
                                dp[i, j, newb] = dp[ii, jj, b] + curcost
                            else:
                                dp[i, j, newb] = min(
                                    dp[i, j, newb],
                                    dp[ii, jj, b] + curcost,
                                )
                            if i == m - 1 and target == newb:
                                # 更新最终结果值
                                res = min(res, dp[i, j, newb])
        # 如果最终结果仍为inf的话则说明不存在这样的涂色方案, 返回-1
        return res if res != float('inf') else -1
