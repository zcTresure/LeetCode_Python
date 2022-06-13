from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
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

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k

        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) >> 1
            x = arr[mid] if mid < len(arr) else 10 ** 9
            if x - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1

        return k - (arr[l - 1] - (l - 1) - 1) + arr[l - 1]


arr = [1, 2, 3, 4]
k = 2
test = Solution()
print(test.findKthPositive(arr, k))
