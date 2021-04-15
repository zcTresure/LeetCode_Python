class Solution:
    def threeConsecutiveOdds(self, arr: list) -> bool:
        count = 0
        for num in arr:
            if num & 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False


arr = [2, 3, 5, 1]
test = Solution()
print(test.threeConsecutiveOdds(arr))
