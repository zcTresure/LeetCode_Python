# File Name:  面试题 04.05. 合法二叉搜索树
# date:       2021/3/28
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
    # 递归
    def isValidBST(self, root: TreeNode) -> bool:
        def heaper(node, left=-float('inf'), right=float('inf')):
            if not node: return True
            if node.val <= left or node.val >= right:
                return False
            if not heaper(node.left, left, node.val):
                return False
            if not heaper(node.right, node.val, right):
                return False
            return True

        return heaper(root)

    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], -float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:  # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
                return False
            inorder = root.val
            root = root.right
        return True


nums = [2, 1, 3]
test = Solution()
root = BinaryTree.build(nums)
print(test.isValidBST(root))
