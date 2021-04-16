# File Name:  剑指 Offer 32 - I. 从上到下打印二叉树
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return None
        root = TreeNode(nums[0])
        nodes, index, n = [root], 1, len(nums)
        for node in nodes:
            if node != None:
                if index == n:
                    return root
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.left)
                index += 1
                if index == n:
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.right)
                index += 1

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
root = test.buildBinaryTree(nums)
print(test.levelOrder(root))
