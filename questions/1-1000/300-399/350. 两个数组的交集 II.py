from collections import Counter
from typing import List


class Solution:
    # 排序
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        print(nums1, nums2)
        ans = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                print(i, j)
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

    # 哈希表
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        m = Counter(nums1)
        intersection = list()
        for num in nums2:
            if (count:= m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
test = Solution()
print(test.intersect(nums1, nums2))
