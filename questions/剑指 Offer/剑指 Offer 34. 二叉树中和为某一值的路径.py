# File Name:  剑指 Offer 34. 二叉树中和为某一值的路径
# date:       2021/4/16
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return None
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
root = test.buildBinaryTree(nums)
print(test.pathSum(root, target))

