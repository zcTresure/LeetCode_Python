# 直接遍历，数组默认升序
# class Solution:
#     def findMagicIndex(self, nums: list) -> int:
#         for i in range(len(nums)):
#             if nums[i] == i:
#                 return i
#         return -1

# 跳着遍历，数组默认升序
# class Solution:
#     def findMagicIndex(self, nums: list) -> int:
#         for i in range(len(nums)):
#             if i == nums[i]:
#                 return i
#             if i < nums[i]:
#                 i = nums[i] - 1
#         return -1


# 利用二分的思想，先找最小区间，数组默认升序
class Solution:
    def findMagicIndex(self, nums: list) -> int:
        def helper(nums: list, left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2
            res = helper(nums, left, mid - 1)
            if res != -1:
                return res
            elif mid == nums[mid]:
                return mid
            else:
                return helper(nums, mid + 1, right)
        return helper(nums, 0, len(nums) - 1)
    


nums = [0, 2, 3, 4, 5]
nums = [-1, 0, 2]
print(Solution.findMagicIndex(1, nums))
