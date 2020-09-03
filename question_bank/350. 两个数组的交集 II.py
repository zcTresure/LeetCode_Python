# 排序
def intersect(self, nums1: list, nums2: list) -> list:
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
def intersect(self, nums1: list, nums2: list) -> list:
    if len(nums1) > len(nums2):
        return self.intersect(nums2, nums1)
    m = collections.Counter()
    for num in nums1:
        m[num] += 1
    intersection = list()
    for num in nums2:
        if (count: = m.get(num, 0)) > 0:
            intersection.append(num)
            m[num] -= 1
            if m[num] == 0:
                m.pop(num)

    return intersection


print(intersect(1, nums1, nums2))
