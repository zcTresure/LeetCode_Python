# File Name:  剑指 Offer 55 - I. 二叉树的深度
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

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

    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        que = [root]
        res = 0
        while que:
            tmp = []
            for node in que:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            que = tmp
            res += 1
        return res


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.maxDepth(root))
