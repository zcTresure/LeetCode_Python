# File Name:  863. 二叉树中所有距离为 K 的结点
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from typing import List
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 查找节点
    def findNode(self, root: TreeNode, target: int) -> TreeNode:
        self.target_node = TreeNode()

        def dfs(node):
            if node:
                if node.val == target:
                    self.target_node = node
                    return
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.target_node

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par = par  # 连接父节点
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:  # 以target为中心向外辐射，到半径为K时返回
                return [node.val for node, _ in queue]
            node, distance = queue.popleft()

            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, distance + 1))
        return []


nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
target = 5
K = 2
test = Solution()
root = BinaryTree.build(nums)
target_node = test.findNode(root, target)
print(test.distanceK(root, target_node, K))
