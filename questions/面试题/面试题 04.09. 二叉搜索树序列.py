# File Name:  面试题 04.09. 二叉搜索树序列
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        result = []

        def findPath(node, tmp, path):
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
            if not tmp:
                result.append(path[:])
                return
            for i, next in enumerate(tmp):
                new_tmp = tmp[:i] + tmp[i + 1:]  # 去除二叉树的根节点
                findPath(next, new_tmp, path + [next.val])

        findPath(root, [], [root.val])
        return result


nums = [2, 1, 3]
test = Solution()
root = test.buildBinaryTree(nums)
result = test.BSTSequences(root)
for tmp in result:
    print(tmp)
