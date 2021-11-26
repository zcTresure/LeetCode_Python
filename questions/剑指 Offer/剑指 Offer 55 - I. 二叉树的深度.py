# File Name:  剑指 Offer 55 - I. 二叉树的深度
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
root = BinaryTree.build(nums)
print(test.maxDepth(root))
