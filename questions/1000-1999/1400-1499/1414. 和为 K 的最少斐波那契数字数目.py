class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = b = 1
        fib = [a, b]
        while a + b <= k:
            fib.append(a + b)
            a, b = b, a + b
        ans = 0
        for num in fib[::-1]:
            if k >= num:
                ans += 1
                k -= num
        return ans


test = Solution()
print(test.findMinFibonacciNumbers(19))
