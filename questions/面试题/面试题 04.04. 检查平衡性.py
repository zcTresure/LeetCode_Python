# File Name:  面试题 04.04. 检查平衡性
# date:       2021/3/24
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
    # 自顶向下的递归
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)

    # 自底向上的递归
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return height(root) >= 0


# nums = [3, 9, 20, None, None, 15, 7]
nums = [1, 2, 2, 3, 3, None, None, 4, 4]
test = Solution()
root = BinaryTree.build(nums)
print(test.isBalanced(root))
