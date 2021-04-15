# File Name:  1302. 层数最深叶子节点的和
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉树的建立
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

    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([root])
        deepest_level_sum = 0
        while queue:
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                node = queue.popleft()
                level_sum += node.val  # 计算机每一层节点和
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            deepest_level_sum = level_sum # 迭代解释时，当前层就为最深层
        return deepest_level_sum


nums = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.deepestLeavesSum(root))
