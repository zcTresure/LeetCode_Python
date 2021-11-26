# File Name:  437. 路径总和 III
# date:       2021/4/10
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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        dp = {}

        def search(node: TreeNode):
            if node:
                search(node.left)
                search(node.right)
                a, b = [], []
                if node.left:
                    a = dp[node.left]
                if node.right:
                    b = dp[node.right]
                temp = [node.val]
                for t in a:
                    temp.append(node.val + t)
                for t in b:
                    temp.append(node.val + t)
                dp[node] = temp

        search(root)
        count = 0
        for node, vals in dp.items():
            for t in vals:
                if t == targetSum:
                    count += 1

        return count


nodes = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
targetSum = 8
test = Solution()
root = BinaryTree.build(nodes)
print(test.pathSum(root, targetSum))
