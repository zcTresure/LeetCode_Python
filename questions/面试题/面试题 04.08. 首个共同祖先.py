# File Name:  面试题 04.08. 首个共同祖先
# date:       2021/4/3
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
    def findVal(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val == val: return root
        self.findVal(root.left, val)
        self.findVal(root.right, val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == q or root == p: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right


nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
test = Solution()
root = BinaryTree.build(nums)
node_p = test.findVal(root, p)
node_q = test.findVal(root, q)
print(node_q)
print(node_q)
print(test.lowestCommonAncestor(root, node_p, node_q).val)
