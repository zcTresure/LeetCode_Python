# File Name:  450. 删除二叉搜索树中的节点
# date:       2021/4/2
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
    # 查找最左节点
    def successor(self, node):
        while node.left:
            node = node.left
        return node.val

    # 查找最右节点
    def predecessor(self, node):
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if key > root.val:  # 目标节点大于根节点，递归寻找右子树
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:  # 目标节点小于根节点，递归寻找左子树
            root.left = self.deleteNode(root.left, key)
        else:  # 找到目标节点
            if not (root.left or root.right):  # 删除节点为叶子节点
                root = None
            elif root.right:  # 删除节点存在右子树
                root.val = self.successor(root.right)  # 找到右子树的最左节点
                root.right = self.deleteNode(root.right, root.val)  # 递归删除右子树最左节点
            else:  # 删除节点存在左子树
                root.val = self.predecessor(root.left)  # 找左子树的最右节点
                root.left = self.deleteNode(root.left, root.val)  # 递归删除左子树最右节点
        return root


nums = [5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]
key = 5
test = Solution()
root = BinaryTree.build(nums)
root = test.deleteNode(root, key)
BinaryTree.preOrder(root)