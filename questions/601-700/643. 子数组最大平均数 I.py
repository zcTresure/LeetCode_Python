class Solution():
    # 和数组 + 滑动窗口
    def findMaxAverage(self, nums: list, k: int) -> float:
        s = [0] * (len(nums))
        s[0] = nums[0]
        for i in range(1, len(nums)):
            s[i] = s[i - 1] + nums[i]
        ans = s[k - 1]
        for i in range(k, len(nums)):
            ans = max(ans, s[i] - s[i - k])
            print(i, i - k)
        return ans / k


    # 滑动窗口
    def findMaxAverage(self, nums: list, k: int) -> float:
        temp = 0
        for i in range(k):
            temp += nums[i]
        ans = temp
        for i in range(k, len(nums)):
            temp = temp + nums[i] - nums[i - k]
            ans = max(ans, temp)
        return ans / k


nums = [1,12,-5,-6,50,3]
k = 4
test = Solution()
print(test.findMaxAverage(nums, k))
