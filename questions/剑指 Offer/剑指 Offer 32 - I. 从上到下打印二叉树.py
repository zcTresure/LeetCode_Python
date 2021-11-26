# File Name:  剑指 Offer 32 - I. 从上到下打印二叉树
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return result


nums = [3, 2, 1, None, None, 2, 3]
test = Solution()
root = BinaryTree.build(nums)
print(test.levelOrder(root))
