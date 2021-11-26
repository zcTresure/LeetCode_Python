# File Name:  814. 二叉树剪枝
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def pruneTree(self, root: TreeNode) -> TreeNode:
        def containOne(node):
            if not node: return False
            a1 = containOne(node.left)
            a2 = containOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containOne(root) else None


nums = [1, None, 0, 0, 1]
test = Solution()
root = BinaryTree.build(nums)
root = test.pruneTree(root)
test.preOrder(root)
