class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(sum(zip(nums[:n], nums[n:]), ()))


class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        for i in range(n * 2):
            j = (2 * i) if i < n else 2 * (i - n) + 1
            nums[j] |= ((nums[i] & 1023) << 10)
        for i in range(2 * n):
            nums[i] >>= 10
        return nums


nums = [2, 5, 1, 3, 4, 7]
n = 3
test = Solution()
print(test.shuffle(nums, n))
