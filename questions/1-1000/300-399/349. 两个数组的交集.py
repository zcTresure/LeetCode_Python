class Solution:
    def intersection_set(self, set1: set, set2: set) -> list:
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: list, nums2: list) -> list:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return self.intersection_set(set1, set2)
        else:
            return self.intersection_set(set2, set1)

    def intersection(self, nums1: list, nums2: list) -> list:
        return list(set(nums1) & set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
test = Solution()
print(test.intersection(nums1, nums2))
