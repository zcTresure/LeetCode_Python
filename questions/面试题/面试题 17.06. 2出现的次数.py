class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            tmp = i
            while tmp != 0:
                ans += 1 if (tmp % 10) ^ 2 == 0 else 0
                tmp //= 10
        return ans

    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        ans = 0
        for i in range(len(s)):
            current = int(s[i])
            high = 0 if s[:i] == '' else int(s[:i])
            low = 0 if s[i + 1:] == '' else int(s[i + 1:])
            if current > 2:
                ans += (high + 1) * (10**len(s[i + 1:]))
            elif current < 2:
                ans += high * (10**len(s[i + 1:]))
            else:
                ans += high * (10**len(s[i + 1:])) + low + 1
        return ans


test = Solution()
print(test.numberOf2sInRange(10000000))
