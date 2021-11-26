# File Name:  687. 最长同值路径
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def heaper(node):
            if not node: return 0
            left_length = heaper(node.left)
            right_length = heaper(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.result = max(self.result, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        heaper(root)
        return self.result


nums = [5, 5, 5, 1, 1, 5]
test = Solution()
root = BinaryTree.build(nums)
print(test.longestUnivaluePath(root))
