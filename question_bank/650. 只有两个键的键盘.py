# 素数分解
class Solution(object):
    def minSteps(self, n):
        ans, d = 0, 2
        while n > 1:
            while n % d == 0:
                print(d, ans)
                ans += d
                n /= d
            d += 1
        return ans


print(Solution.minSteps(1, 10))
