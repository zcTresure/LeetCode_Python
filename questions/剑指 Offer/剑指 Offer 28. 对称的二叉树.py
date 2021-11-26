# File Name:  剑指 Offer 28. 对称的二叉树
# date:       2021/3/29
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
    def isSymmetric(self, root: TreeNode) -> bool:
        def heaper(L, R):
            if not L and not R: return True  # 左节点和右节点都不存在，二叉树对称
            if not L or not R or L.val != R.val: return False
            # 递归检查左节点的左孩子和右节点的右孩子 或 左节点的右孩子和右节点的左孩子是否对称
            return heaper(L.left, R.right) and heaper(L.right, R.left)

        # 根节点为空时对称二叉树，否则递归检查左右子树
        return heaper(root.left, root.right) if root else True


nums = [1, 2, 2, 3, 4, 4, 3]
test = Solution()
root = BinaryTree.build(nums)
print(test.isSymmetric(root))