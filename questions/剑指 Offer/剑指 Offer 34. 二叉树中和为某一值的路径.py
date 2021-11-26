# File Name:  剑指 Offer 34. 二叉树中和为某一值的路径
# date:       2021/4/16
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


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(node, path, target):
            if not node: return
            target -= node.val
            path.append(node.val)
            if target == 0 and not (node.left or node.right):
                result.append(path[:])
            dfs(node.left, path, target)
            dfs(node.right, path, target)
            target += node.val
            path.pop()

        result = []
        dfs(root, [], target)
        return result


nums = [5, 4]
target = 5
test = Solution()
root = BinaryTree.build(nums)
print(test.pathSum(root, target))

