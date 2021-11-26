# File Name:  669. 修剪二叉搜索树
# date:       2021/4/3
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 层次遍历
    def levelOrder(self, root: TreeNode) -> None:
        q = deque([root])
        while q:
            node = q.popleft()
            if node: print(node.val, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


nums = [3, 0, 4, None, 2, None, None, 1]
low = 1
high = 3
test = Solution()
root = BinaryTree.build(nums)
root = test.trimBST(root, low, high)
test.levelOrder(root)
