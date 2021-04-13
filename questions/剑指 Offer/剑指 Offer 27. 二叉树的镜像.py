# File Name:  剑指 Offer 27. 二叉树的镜像
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        left, right = root.left, root.right
        root.left, root.right = right, left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root

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


nums = [4, 2, 7, 1, 3, 6, 9]
test = Solution()
root = test.buildBinaryTree(nums)
root = test.mirrorTree(root)
test.levelOrder(root)
