class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1


nums = [-1, -1, 0, 1, 1, 0]
test = Solution()
print(test.pivotIndex(nums))
