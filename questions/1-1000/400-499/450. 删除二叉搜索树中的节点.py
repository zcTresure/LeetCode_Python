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
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def successor(self, node):  # One step right and then always left
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self, node):  # One step left and then always right
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.preOrder(root)
        print()
        if not root: return None
        if key > root.val:  # delete from the right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:  # delete from the left subtree
            root.left = self.deleteNode(root.left, key)
        else:  # delete the current node
            if not (root.left or root.right):  # the node is a leaf
                root = None
            elif root.right:  # the node is not a leaf and has a right child
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:  # the node is not a leaf, has no right child, and has a left child
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root


nums = [5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]
key = 5
test = Solution()
root = BinaryTree.build(nums)
root = test.deleteNode(root, key)
test.preOrder(root)
