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
        if not root:  # 二叉树不存在，
            return True
        self.val = root.val  # 记录根节点值

        def dfs(node: TreeNode) -> bool:
            if not node:  # 节点为空
                return True
            if node.val != self.val:  # 节点值与根节点值不相同
                return False
            left = dfs(node.left)  # 递归搜索左孩子
            right = dfs(node.right)  # 递归搜索右孩子
            return left and right

        return dfs(root)


nums = [1, 1, 1, 1, 1, None, 2]
root = BinaryTree.build(nums)
print(Solution().isUnivalTree(root))
