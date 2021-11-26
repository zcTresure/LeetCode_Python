# File Name:  1325. 删除给定值的叶子节点
# date:       2021/4/15
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
    def levelOrder(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                print(node.val, end='')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q:
                    print(end=' ')
        print()

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root


nums = [1, 2, 3, 2, None, 2, 4]
target = 2
test = Solution()
root = BinaryTree.build(nums)
root = test.removeLeafNodes(root, target)
test.levelOrder(root)
