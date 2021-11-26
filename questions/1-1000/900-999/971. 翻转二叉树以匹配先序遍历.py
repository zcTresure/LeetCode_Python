# File Name:  971. 翻转二叉树以匹配先序遍历
# date:       2021/3/25
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = []
        self.i = 0

        def dfs(node: root):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1
                if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped


test = Solution()
nums = [1, 2, 3]
voyage = [1, 3, 2]
root = BinaryTree.build(nums)
print(test.flipMatchVoyage(root, voyage))
