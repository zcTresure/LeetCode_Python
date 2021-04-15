class Solution:
    def maxSumDivThree(self, nums: list) -> int:
        sumNums = 0
        class1 = [1000000] * 3
        class2 = [1000000] * 3
        for i in range(len(nums)):
            sumNums += nums[i]
            if nums[i] % 3 == 1:
                class1[2] = nums[i]
                class1.sort()
            elif nums[i] % 3 == 2:
                class2[2] = nums[i]
                class2.sort()
        if sumNums % 3 == 0:
            return sumNums
        elif sumNums % 3 == 1:
            return sumNums - min(class1[0], class2[0] + class2[1])
        else:
            return sumNums - min(class2[0], class1[0] + class1[1])


nums = [2, 3, 36, 8, 32, 38, 3, 30, 13, 40]
test = Solution()
print(test.maxSumDivThree(nums))
