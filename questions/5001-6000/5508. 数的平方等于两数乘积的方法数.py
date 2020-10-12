import collections


class Solution:
    def numTriplets(self, nums1: list, nums2: list) -> int:
        def initPower(arr: list) -> dict:
            dic = {}
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    t = arr[i] * arr[j]
                    if t not in dic:
                        dic[t] = 1
                    else:
                        dic[t] += 1
            return dic

        def sumAns(nums: list, dic: dict) -> int:
            ans = 0
            for num in nums:
                t = num * num
                if t in dic:
                    ans += dic[t]
            return ans

        dic1 = initPower(nums1)
        dic2 = initPower(nums2)
        return sumAns(nums1, dic2) + sumAns(nums2, dic1)


nums1 = [1, 1]
nums2 = [1, 1, 1]
test = Solution()
print(test.numTriplets(nums1, nums2))
