# File Name:  965. 单值二叉树
# date:       2021/4/2
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        self.val = root.val

        def dfs(node):
            if not node: return True
            if node.val != self.val: return False
            L, R = dfs(node.left), dfs(node.right)
            return L and R

        return dfs(root)


nums = [1]
test = Solution()
root = BinaryTree.build(nums)
print(test.isUnivalTree(root))
