# File Name:  1356. 根据数字二进制下 1 的数目排序
# date:       2020/11/06
# encode:      UTF-8


from collections import defaultdict
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bins = defaultdict(list)
        for num in arr:
            count, tmp = 0, num
            while tmp:
                count += tmp % 2
                tmp //= 2
            bins[count].append(num)
        res = list()
        for i in range(15):
            if bins[i]:
                res += sorted(bins[i])
        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        bins = [0] * 10001
        for i in range(1, 10001):
            bins[i] = bins[i >> 1] + i % 2
        dic = defaultdict(list)
        for num in arr:
            dic[bins[num]].append(num)
        res = list()
        for i in range(15):
            if dic[i]:
                res += sorted(dic[i])
        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test = Solution()
print(test.sortByBits(arr))
