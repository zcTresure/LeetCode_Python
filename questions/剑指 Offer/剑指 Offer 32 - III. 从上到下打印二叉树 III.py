# Date:       2021/4/1
# Coding:      UTF-8
__author__ = "zcTresure"

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

    # 层序遍历 + 双端队列
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], deque([root])
        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2: level.appendleft(node.val)  # 偶数层 -> 队列头部
                else: level.append(node.val)  # 奇数层 -> 队列尾部
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(level))
        return res


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.levelOrder(root))
