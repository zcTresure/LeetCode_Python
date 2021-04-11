# File Name:  264. 丑数 II
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'

import heapq


class Solution:
    # 最小堆
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        heap = [1]
        seen = {1}
        for _ in range(n - 1):
            current = heapq.heappop(heap)
            for factor in factors:
                if (next := current * factor) not in seen:
                    seen.add(next)
                    heapq.heappush(heap, next)

        return heapq.heappop(heap)

    # 动态规划
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] + [0] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2: p2 += 1
            if dp[i] == num3: p3 += 1
            if dp[i] == num5: p5 += 1
        return dp[n - 1]


n = int(input("输入整数："))
test = Solution()
print(f"第{n}个丑数为:{test.nthUglyNumber(n)}")
