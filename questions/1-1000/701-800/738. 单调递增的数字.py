# Date:       2020/12/15
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        i = 1
        res = N
        while i <= res // 10:
            n = res // i % 100
            i = i * 10
            if n // 10 > n % 10:
                res = res // i * i - 1
        return res

    def monotoneIncreasingDigits(self, N: int) -> int:
        digit = list(str(N))
        n = len(digit)
        for i in range(n - 1, 0, -1):
            if digit[i] < digit[i - 1]:
                digit[i - 1] = str(int(digit[i - 1]) - 1)
                digit[i:] = ['9'] * (n - i)
        return int(''.join(digit))


N = 101
test = Solution()
print(test.monotoneIncreasingDigits(N))
