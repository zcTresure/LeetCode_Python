# File Name:  面试题 17.12. BiNode
# date:       2021/4/13
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
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.ans = self.pre = None

        def inorder(node):
            if not node: return None
            inorder(node.left)
            node.left = None
            if self.pre: self.pre.right = node
            if not self.pre: self.ans = node
            self.pre = node
            inorder(node.right)

        inorder(root)
        return self.ans


nums = [4, 2, 5, 1, 3, None, 6, 0]
test = Solution()
root = BinaryTree.build(nums)
test.preOrder(root)
print()
root = test.convertBiNode(root)
test.preOrder(root)
