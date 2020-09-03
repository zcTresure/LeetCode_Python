# 记忆数组记录数组嵌套
# class Solution:
#     def arrayNesting(self, nums: list) -> int:
#         n = len(nums)
#         memo = [0] * n  # 记忆数组
#         ans = temp = 0
#         for i in range(n):
#             if memo[i] == 1:
#                 continue
#             temp, index, memo[i] = 1, nums[i], 1
#             while True:
#                 if memo[index] == 0:
#                     memo[index] = 1
#                     temp += 1
#                 else:
#                     ans = max(ans, temp)
#                     break
#                 index = nums[index]
#         return ans

# 原始数组 nums本身中标记访问过的元素  
class Solution:
    def arrayNesting(self, nums: list) -> int:
        n = len(nums)
        ans = temp = 0
        for i in range(n):
            temp, pre = 0, i
            while pre < n:
                temp += 1
                cur = pre
                pre = nums[pre]
                nums[cur] = n
            ans = max(ans, temp - 1)

        return ans


A = [5, 4, 0, 3, 1, 6, 2]
print(Solution.arrayNesting(1, A))
