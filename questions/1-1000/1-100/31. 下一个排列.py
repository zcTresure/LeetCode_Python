# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums: list) -> None:
        size = len(nums)
        if size <= 1:
            return nums
        pos = -1
        pos1 = 0
        for i in range(size - 1):  # 遍历到倒数第二个位置，因为每个元素要与之后的元素比较，防止溢出
            if nums[i] < nums[i + 1]:
                pos = i
            if pos != -1 and nums[i] > nums[pos]:
                pos1 = i
        if pos != -1 and nums[-1] > nums[pos]:  # 弥补之前最后一个元素未被遍历到的漏洞
            pos1 = size - 1
        if pos == -1:  # 没有“顺序对”
            nums[:] = nums[::-1]
        else:
            nums[pos], nums[pos1] = nums[pos1], nums[pos]
            nums[:] = nums[:pos + 1] + nums[size - 1:pos:-1]


nums = [2, 3, 1]
test = Solution()
test.nextPermutation(nums)
print(nums)
