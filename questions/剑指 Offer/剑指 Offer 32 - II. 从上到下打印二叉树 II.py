# File Name:  剑指 Offer 32 - II. 从上到下打印二叉树 II
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
root = BinaryTree.build(nums)
print(test.levelOrder(root))
