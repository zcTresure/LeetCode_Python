# File Name:  515. 在每个树行中找最大值
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque


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

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)  # 每一层节点数
            tmp = []  # 记录每一层节点值
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(tmp))
        return result


nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test = Solution()
root = test.buildBinaryTree(nodes)
print(test.largestValues(root))
