# File Name:  655. 输出二叉树
# date:       2021/4/12
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

    def printTree(self, root: TreeNode) -> List[List[str]]:
        heigh = self.getHeight(root)
        result = [[""] * ((1 << heigh) - 1) for _ in range(heigh)]  # 矩阵的宽度为树最深一层的最大宽度
        self.fill(result, root, 0, 0, len(result[0]))
        return result

    def fill(self, result: list, root: TreeNode, i, left, right):
        if not root: return
        result[i][(left + right) // 2] = str(root.val)
        self.fill(result, root.left, i + 1, left, (left + right) // 2)
        self.fill(result, root.right, i + 1, (left + right + 1) // 2, right)

    # 二叉树的深度
    def getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


nums = [1, 2, 5, 3, None, None, None, 4]
test = Solution()
root = test.buildBinaryTree(nums)
result = test.printTree(root)
for i in range(len(result)):
    print(result[i])
