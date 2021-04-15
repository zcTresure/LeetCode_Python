# File Name:  1530. 好叶子节点对的数量
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


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
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root: TreeNode, distance: int) -> (List[int], int):
            depths = [0] * (distance + 1)
            is_leaf = not root.left and not root.right  # 判断是否为叶子节点
            if is_leaf:  # 是叶子节点，深度加1，返回结果
                depths[0] = 1
                return (depths, 0)
            # 记录左右节点的深度
            left_depths, right_depths = [0] * (distance + 1), [0] * (distance + 1)
            left_count = right_count = 0
            if root.left: left_depths, left_count = dfs(root.left, distance)  # 非叶子节点，继续深搜
            if root.right: right_depths, right_count = dfs(root.right, distance)
            for i in range(distance):
                depths[i + 1] += (left_depths[i] + right_depths[i])
            cnt = 0
            for i in range(distance + 1):
                for j in range(distance - i - 1):
                    cnt += left_depths[i] * right_depths[j]
            return (depths, cnt + left_count + right_count)

        (_, ret) = dfs(root, distance)
        return ret


nums = [1, 2, 3, 4, 5, 6, 7]
distance = 3
test = Solution()
root = test.buildBinaryTree(nums)
test.preOrder(root)
print()
print(test.countPairs(root, distance))
