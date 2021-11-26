# File Name:  1161. 最大层内元素和
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
root = BinaryTree.build(nums)
print(test.maxLevelSum(root))
