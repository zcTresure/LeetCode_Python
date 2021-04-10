# File Name:  437. 路径总和 III
# date:       2021/4/10
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        nodes, index, n = [root], 1, len(nums)
        for node in nodes:
            if node != None:
                if index == n:
                    return root
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.left)
                index += 1
                if index == n:
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.right)
                index += 1

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
root = test.buildBinaryTree(nodes)
print(test.pathSum(root, targetSum))
