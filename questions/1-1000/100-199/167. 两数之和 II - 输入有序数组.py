class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []


numbers = [2, 7, 11, 15]
target = 9
test = Solution()
print(test.twoSum(numbers, target))
