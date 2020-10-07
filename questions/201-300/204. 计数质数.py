class Solution:
    # 暴力法
    def countPrimes(self, n: int) -> int:
        ans = 0
        for i in range(2, n):
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

    # 暴力 + 优化
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        ans = 1
        for i in range(2, n):
            if i & 1 == 0:
                continue
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

    # 筛法
    def countPrimes(self, n: int) -> int:
        ans = 0
        prime = [True] * n
        for i in range(2, n):
            if prime[i]:
                ans += 1
                for j in range(i + i, n, i):
                    prime[j] = False
        return ans


n = 10
test = Solution()
print(test.countPrimes((n)))
