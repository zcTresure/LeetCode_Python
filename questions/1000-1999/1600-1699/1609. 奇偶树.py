# File Name:  1609. 奇偶树
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

# Definition for a binary tree node.
from collections import deque


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

    def isEvenOddTree(self, root: TreeNode) -> bool:  # 层此遍历
        queue, level = deque([root]), 0
        while queue:
            n = len(queue)
            odd_val, even_val = float('-inf'), float('inf')
            for _ in range(n):
                node = queue.popleft()
                if node.val % 2 == level % 2:  # 偶数层有偶数 或 奇数层有奇数时 返回
                    return False
                if level % 2 == 0:
                    if odd_val >= node.val:  # 偶数层严格递增
                        return False
                    odd_val = node.val
                else:
                    if even_val <= node.val:  # 奇数层严格递减
                        return False
                    even_val = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return True


root = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
test = Solution()
root = test.buildBinaryTree(root)
print(test.isEvenOddTree(root))
