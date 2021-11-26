# Date:       2021/4/1
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 层序遍历 + 双端队列
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], deque([root])
        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2: level.appendleft(node.val)  # 偶数层 -> 队列头部
                else: level.append(node.val)  # 奇数层 -> 队列尾部
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(level))
        return res


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = BinaryTree.build(nums)
print(test.levelOrder(root))
