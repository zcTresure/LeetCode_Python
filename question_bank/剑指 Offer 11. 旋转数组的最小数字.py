class Solution:
    def minArray(self, numbers: list) -> int:
        l, h = 0, len(numbers) - 1
        while l < h:
            m = (h + l) >> 1
            if numbers[m] < numbers[h]:
                h = m
            elif numbers[m] > numbers[h]:
                l = m + 1
            else:
                h -= 1
        return numbers[l]


nums = [3, 4, 5, 1, 2, 2]
nums = [2, 2, 2, 0, 1, 1]
test = Solution()
print(test.minArray(nums))
