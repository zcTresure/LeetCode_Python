class Solution:
    def missingTwo(self, nums: list) -> list:
        # 方法1 : cyclic sort
        ret = []
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            # 因为缺两个，就只拍从1到n的，n+1与n+2 补位给缺失的元素
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                ret.append(i + 1)
        if len(ret) == 1:
            # 这里怎么处理？
            # 上面找到的都是[1...n]的，所以缺的可能性有两种 n + 1 或者 n + 2
            if n + 1 in nums:
                ret.append(n + 2)
            else:
                ret.append(n + 1)
        elif len(ret) == 0:
            return [n + 1, n + 2]
        return ret

    def missingTwo(self, nums: list) -> list:
        n = len(nums)
        sumTwoBlank = (n + 2) * (n + 3) // 2 - sum(nums)
        div = sumTwoBlank / 2
        # 分组异或
        a, b = 0, 0
        for num in nums:
            if num >= div:
                a ^= num
            else:
                b ^= num
        for i in range(1, n + 3):
            if i >= div:
                a ^= i
            else:
                b ^= i
        return [a, b]


nums = [2, 3]
test = Solution()
print(test.missingTwo(nums))
