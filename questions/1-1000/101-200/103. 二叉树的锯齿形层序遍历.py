# Date:       2020/12/22
# Coding:      UTF-8
__author__ = "zcTresure"

# 题目
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def constructBTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        nodeQueue = deque()
        nodeQueue.append(root)
        # 判断每一层是从左到右还是从右到左
        Orderleft = True

        while nodeQueue:
            # 存储二叉树每一层的值
            levelList = deque()
            n = len(nodeQueue)
            for i in range(n):
                node = nodeQueue.popleft()
                if Orderleft:  # 从左到右存储
                    levelList.append(node.val)
                else:  # 从右到左存储
                    levelList.appendleft(node.val)
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            ans.append(list(levelList))
            # 第一层是从左到右存储，后面每一层和上一层的顺序相反
            Orderleft = not Orderleft
        return ans


nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.constructBTree(nums)
print(test.zigzagLevelOrder(root))
