from collections import Counter


class Solution:
    # 求和
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2

    # 计数
    def singleNumber(self, nums):
        hashmap = Counter(nums)
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k

    # 位运算
    def singleNumber(self, nums: list) -> int:
        seen_once = seen_twice = 0

        print("once  ", bin(seen_once))
        print("twice ", bin(seen_twice))
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
            print("once  ", bin(seen_once))
            print("twice ", bin(seen_twice))
            print('----------------')

        return seen_once


nums = [4, 10, 4, 4]
test = Solution()
print(test.singleNumber(nums))
