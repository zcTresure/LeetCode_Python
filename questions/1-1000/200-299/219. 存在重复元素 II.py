class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        dic = dict()
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            else:
                if k >= i - dic[num]:
                    return True
                dic[num] = i
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
test = Solution()
print(test.containsNearbyDuplicate(nums, k))
