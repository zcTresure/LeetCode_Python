# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"

import bisect


class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        sumNum = [0]
        for num in nums:
            sumNum.append(sumNum[-1] + num)
        return self.contRangeSumRecursive(sumNum, lower, upper, 0, len(sumNum) - 1)

    def contRangeSumRecursive(self, sumNum: list, lower: int, upper: int, left: int, right: int) -> int:
        if left == right:
            return 0
        mid = (left + right) // 2
        n1 = self.contRangeSumRecursive(sumNum, lower, upper, left, mid)
        n2 = self.contRangeSumRecursive(sumNum, lower, upper, mid + 1, right)
        res = n1 + n2
        # 首先统计下标对的数量
        i, l, r = left, mid + 1, mid + 1
        while i <= mid:
            while l <= right and sumNum[l] - sumNum[i] < lower:
                l += 1
            while r <= right and sumNum[r] - sumNum[i] <= upper:
                r += 1
            res += (r - l)
            i += 1
        # 合并两耳光排序数组
        tmp = [0] * (right - left + 1)
        p1, p2, p = left, mid + 1, 0
        while p1 <= mid or p2 <= right:
            if p1 > mid:
                tmp[p] = sumNum[p2]
                p2 += 1
            elif p2 > right:
                tmp[p] = sumNum[p1]
                p1 += 1
            else:
                if sumNum[p1] < sumNum[p2]:
                    tmp[p] = sumNum[p1]
                    p1 += 1
                else:
                    tmp[p] = sumNum[p2]
                    p2 += 1
            p += 1
        for i in range(len(tmp)):
            sumNum[left + i] = tmp[i]
        return res

    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res


nums = [-2, 5, -1]
lower, upper = -2, 2
test = Solution()
print(test.countRangeSum(nums, lower, upper))
