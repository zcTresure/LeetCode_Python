# File Name:  1305. 两棵二叉搜索树中的所有元素
# date:       2021/4/15
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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = list()

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root1)
        dfs(root2)
        ans.sort()
        return ans

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, val):
            if not root: return
            inorder(root.left, val)
            val.append(root.val)
            inorder(root.right, val)

        val1, val2 = list(), list()
        inorder(root1, val1)
        inorder(root2, val2)
        length1, length2 = len(val1), len(val2)
        index1 = index2 = 0
        result = []
        while index1 < length1 or index2 < length2:
            if index1 < length1 and (index2 == length2 or val1[index1] < val2[index2]):
                result.append(val1[index1])
                index1 += 1
            else:
                result.append(val2[index2])
                index2 += 1
        return result


nums1 = [2, 1, 4]
nums2 = [1, 0, 3]
test = Solution()
root1 = test.buildBinaryTree(nums1)
root2 = test.buildBinaryTree(nums2)
print(test.getAllElements(root1, root2))
