class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        tmp = {}
        nums = sorted(list(set(arr)))
        for i, num in enumerate(nums):
            tmp[num] = i + 1
        return [tmp[i] for i in arr]


arr = [10, 10, 20, 30]
test = Solution()
print(test.arrayRankTransform(arr))
