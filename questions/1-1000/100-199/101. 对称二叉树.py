# File Name:  101. 对称二叉树
# date:       2021/4/11
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
    def isSymmetric(self, root: TreeNode) -> bool:
        def heaper(lefts, rights):
            if not lefts and not rights: return True
            if not lefts or not rights:
                return False
            if lefts.val != rights.val or (not lefts and rights) or (lefts and not rights):
                return False
            return heaper(lefts.left, rights.right) and heaper(lefts.right, rights.left)

        return heaper(root.left, root.right)


nodes = [1, 2, 2, 3, 4, 4,3]
test = Solution()
root = BinaryTree.build(nodes)
print(test.isSymmetric(root))
