class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** (len(bin(num)) - 2) - num - 1

num = 5
test = Solution()
print(test.findComplement(num))
