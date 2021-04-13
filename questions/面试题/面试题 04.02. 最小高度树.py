# File Name:  面试题 04.02. 最小高度树
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from  collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        def dfs(node, nums):
            if not nums: return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(node, nums[:mid])
            node.right = dfs(node, nums[mid + 1:])
            return node

        return dfs(None, nums)

    # 层次遍历
    def levelOrder(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                print(node.val, end='')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q:
                    print(end=' ')
        print()

nums = [-10,-3,0,5,9]
test = Solution()
root = test.sortedArrayToBST(nums)
test.levelOrder(root)
