# -*- coding: utf-8 -*-
# File:     278. 第一个错误的版本.py
# Date:     2021/6/14
# Software: PyCharm
__author__ = 'zcFang'


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    return version == bad


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


bad, n = 4, 5
print(Solution().firstBadVersion(n))
