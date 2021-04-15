# File Name:  1161. 最大层内元素和
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

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

    def maxLevelSum(self, root: TreeNode) -> int:
        max_level = level = 0
        max_level_sum = float("-inf")
        queue = deque([root])
        while queue:
            level += 1
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                node = queue.popleft()
                level_sum += node.val  # 计算机每一层节点和
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if max_level_sum < level_sum:  # 更新最大层
                max_level_sum = level_sum
                max_level = level
        return max_level


nums = [1, 7, 0, 7, -8, None, None]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.maxLevelSum(root))
