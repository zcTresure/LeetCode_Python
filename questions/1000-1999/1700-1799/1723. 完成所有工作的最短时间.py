# -*- coding: utf-8 -*-
# File:     1723. 完成所有工作的最短时间.py
# Date:     2021/7/2
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)
            groups = [0] * k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            # print(arr, groups, limit)
            if not arr: return True  # 分完，则方案可行
            v = arr.pop()
            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v
                    # 如果这个工人分活失败（给他分配这个任务后所有的尝试都是失败的），则剪枝，因为也没必要再往后试了，其他人也会出现一样的情况
                    if groups[i] == 0:
                        break
            arr.append(v)
            return False

        # 每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


jobs = [3, 2, 3]
k = 3
print(Solution().minimumTimeRequired(jobs, k))
