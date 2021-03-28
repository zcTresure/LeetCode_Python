# File Name:  剑指 Offer 32 - II. 从上到下打印二叉树 II
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(level)
        return ans


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.levelOrder(root))
