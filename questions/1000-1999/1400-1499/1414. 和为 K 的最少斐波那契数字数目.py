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

    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        ans, i = 0, len(fib) - 1
        while k:
            if k >= fib[i]:
                k -= fib[i]
                ans += 1
            i -= 1
        return ans


test = Solution()
print(test.findMinFibonacciNumbers(19))
