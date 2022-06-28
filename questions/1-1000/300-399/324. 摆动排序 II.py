# -*- coding: utf-8 -*-
# File:      324. 摆动排序 II.py
# DATA:      2022/6/28
# Software:  PyCharm
import datetime
from random import randint, seed, shuffle
from typing import List


def quickSelect(a: List[int], k: int) -> int:
    seed(datetime.datetime.now())
    shuffle(a)
    l, r = 0, len(a) - 1
    while l < r:
        pivot = a[l]
        i, j = l, r + 1
        while True:
            i += 1
            while i < r and a[i] < pivot:
                i += 1
            j -= 1
            while j > l and a[j] > pivot:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], pivot
        if j == k:
            break
        if j < k:
            l = j + 1
        else:
            r = j - 1
    return a[k]


class Helper:
    @staticmethod
    def quickSelect(nums: List[int], left: int, right: int, index: int) -> int:
        q = Helper().randomPartition(nums, left, right)
        if q == index:
            return nums[q]
        if q < index:
            return Helper.quickSelect(nums, q + 1, right, index)
        return Helper.quickSelect(nums, left, q - 1, index)

    @staticmethod
    def randomPartition(nums: List[int], left: int, right: int) -> int:
        i = randint(left, right)
        nums[right], nums[i] = nums[i], nums[right]
        return Helper.partition(nums, left, right)

    @staticmethod
    def partition(nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        index = left - 1
        for j in range(left, right):
            if nums[j] < pivot:
                index += 1
                nums[index], nums[j] = nums[j], nums[index]
        nums[index + 1], nums[right] = nums[right], nums[index + 1]
        return index + 1


class Solution:
    # 排序
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1

    # 三向切分
    def wiggleSort1(self, nums: List[int]) -> None:
        n = len(nums)
        x = (n + 1) // 2
        seed(datetime.datetime.now())
        target = Helper.quickSelect(nums, 0, n - 1, x - 1)
        k, i, j = 0, 0, n - 1
        while k <= j:
            if nums[k] > target:
                while j > k and nums[j] > target:
                    j -= 1
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            if nums[k] < target:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            k += 1
        arr = nums.copy()
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1

    # 递归优化
    def wiggleSort2(self, nums: List[int]) -> None:
        n = len(nums)
        x = (n + 1) // 2
        target = quickSelect(nums, x - 1)

        transAddress = lambda i: (2 * n - 2 * i - 1) % (n | 1)
        k, i, j = 0, 0, n - 1
        while k <= j:
            tk = transAddress(k)
            if nums[tk] > target:
                while j > k and nums[transAddress(j)] > target:
                    j -= 1
                tj = transAddress(j)
                nums[tk], nums[tj] = nums[tj], nums[tk]
                j -= 1
            if nums[tk] < target:
                ti = transAddress(i)
                nums[tk], nums[ti] = nums[ti], nums[tk]
                i += 1
            k += 1


nums = [1, 5, 1, 1, 6, 4]
Solution().wiggleSort1(nums)
print(nums)
