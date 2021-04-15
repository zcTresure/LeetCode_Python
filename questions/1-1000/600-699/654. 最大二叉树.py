# File Name:  654. 最大二叉树
# date:       2021/4/12
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        def heaper(nums, root=None):
            if not nums: return None
            max_index = nums.index(max(nums))  # 数组最大值下标
            root = TreeNode(nums[max_index])  # 以最大值构建根节点
            root.left = heaper(nums[:max_index], root)  # 递归建立左子树最最大根
            root.right = heaper(nums[max_index + 1:], root)  # 递归建立右子树最最大根
            return root

        return heaper(nums)

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


nums = [3, 2, 1]
test = Solution()
root = test.constructMaximumBinaryTree(nums)
test.levelOrder(root)
