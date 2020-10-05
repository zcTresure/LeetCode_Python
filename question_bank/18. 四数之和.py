class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        res = list()
        if not nums or len(nums) < 4:
            return res
        nums.sort()
        lens = len(nums)
        for i in range(lens - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[lens - 3] + nums[lens - 2] + nums[lens - 1] < target:
                continue
            for j in range(i + 1, lens - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[lens - 2] + nums[lens - 1] < target:
                    continue
                left, right = j + 1, lens - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
test = Solution()
print(test.fourSum(nums, target))
