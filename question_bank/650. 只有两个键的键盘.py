# 素数分解
class Solution(object):
    def minSteps(self, n):
        ans, d = 0, 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans

test = Solution()
print(test.minSteps(10))
