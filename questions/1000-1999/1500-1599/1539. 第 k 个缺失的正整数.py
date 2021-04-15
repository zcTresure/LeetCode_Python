class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        count, num, index = 0, 1, 0
        while index < len(arr):
            if num == arr[index]:
                index += 1
            else:
                count += 1
                if count == k:
                    return num
            num += 1
        return arr[index - 1] + k - count


arr = [1, 2, 3, 4]
k = 2
test = Solution()
print(test.findKthPositive(arr, k))
