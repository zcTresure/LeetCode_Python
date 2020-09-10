class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3:
            return False
        while n != 1:
            if n % 3 == 0:
                print(1)
                n /= 3
            else:
                return False
        return True


print(Solution().isPowerOfThree(45))
