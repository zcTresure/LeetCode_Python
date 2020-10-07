class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3:
            return False
        while n != 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return True


test = Solution()
print(test.isPowerOfThree(45))
