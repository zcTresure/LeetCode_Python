# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else x + max(arr1))

    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))

    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1
        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
test = Solution()
print(test.relativeSortArray(arr1, arr2))
