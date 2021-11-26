# File Name:  1026. 节点与其祖先之间的最大差值
# date:       2021/4/14
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
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = -1

        def dfs(node, max_val, min_val):
            if not node:
                self.result = max(self.result, max_val - min_val)
            else:
                max_val, min_val = max(max_val, node.val), min(min_val, node.val)
                dfs(node.left, max_val, min_val)
                dfs(node.right, max_val, min_val)

        dfs(root, 0, 100001)
        return self.result


nums = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
test = Solution()
root = BinaryTree.build(nums)
print(test.maxAncestorDiff(root))
