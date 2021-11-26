# File Name:  700. 二叉搜索树中的搜索
# date:       2021/4/13
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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.node = None

        def dfs(node):
            if not node: return
            if node.val == val:
                self.node = node
                return
            elif node.val > val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        return self.node

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if root.val == val:
            return root
        return root.left if root.val > val else root.right


nums = [4, 2, 7, 1, 3]
val = 2
test = Solution()
root = BinaryTree.build(nums)
node = test.searchBST(root, val)
print(node.val) if node else print(0)
