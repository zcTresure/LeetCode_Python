# -*- coding: utf-8 -*-
# File:     1707. 与数组中元素的最大异或值.py
# Date:     2021/5/23
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Trie:  # 字典树
    L = 30

    def __init__(self):
        self.left = None
        self.right = None
        self.min_value = float('inf')

    def insert(self, val: int):
        node = self
        node.min_value = min(node.min_value, val)
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1  # 取出当前二进制位
            if bit == 0:  # 当前二进制位为0
                if not node.left:  # 左子树不存在 构建左子树
                    node.left = Trie()
                node = node.left  # 迭代进入左子树
            else:  # 当前二进制位为1
                if not node.right:  # 右子树不存在 构建右子树
                    node.right = Trie()
                node = node.right  # 迭代进入右子树
            node.min_value = min(node.min_value, val)

    def getMaxXor(self, val: int) -> int:  # 获取最大的 异或值
        ans, node = 0, self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1  # 取出当前二进制位
            check = False  # 初始化当前位为假
            if bit == 0:  # 当前二进制位为0
                if node.right:  # 因为是求异或值。所以进入右子树
                    node = node.right
                    check = True  # 当前位标记为真
                else:  # 右子树不存在则进入左子树
                    node = node.left
            else:  # 当前二进制位为1
                if node.left:  # 因为是求异或值。所以进入右子树
                    node = node.left
                    check = True  # 当前位标记为真
                else:  # 左子树不存在则进入右子树
                    node = node.right
            if check:  # 右子树或左子树存在 异或值增加当前二进制位
                ans |= 1 << i
        return ans

    def getMaxXorWithLimit(self, val: int, limit: int) -> int:
        node = self
        if node.min_value > limit:
            return -1
        ans = 0
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False  # 初始化当前位为假
            if bit == 0:  # 当前二进制位为0
                if node.right and node.right.min_value <= limit:  # 因为是求异或值。所以进入右子树
                    node = node.right
                    check = True  # 当前位标记为真
                else:  # 右子树不存在则进入左子树
                    node = node.left
            else:  # 当前二进制位为1
                if node.left and node.left.min_value <= limit:  # 因为是求异或值。所以进入右子树
                    node = node.left
                    check = True  # 当前位标记为真
                else:  # 左子树不存在则进入右子树
                    node = node.right
            if check:  # 右子树或左子树存在 异或值增加当前二进制位
                ans |= 1 << i
        return ans


class Solution:
    # def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    #     n, q = len(nums), len(queries)
    #     nums.sort()
    #     queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])
    #     ans = [0] * q
    #     t = Trie()
    #     idx = 0
    #     for x, m, qid in queries:
    #         while idx < n and nums[idx] <= m:
    #             t.insert(nums[idx])
    #             idx += 1
    #         if idx == 0:  # 字典树为空
    #             ans[qid] = -1
    #         else:
    #             ans[qid] = t.getMaxXor(x)
    #     return ans

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        t = Trie()
        for val in nums:
            t.insert(val)
        q = len(queries)
        ans = [0] * q
        for i, (x, m) in enumerate(queries):
            ans[i] = t.getMaxXorWithLimit(x, m)
        return ans


# nums = [0, 1, 2, 3, 4]
# queries = [[3, 1], [1, 3], [5, 6]]
nums = [5, 2, 4, 6, 6, 3]
queries = [[12, 4], [8, 1], [6, 3]]
test = Solution()
print(test.maximizeXor(nums, queries))
