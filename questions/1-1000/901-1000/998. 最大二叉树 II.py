# File Name:  998. 最大二叉树 II
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


nums =[4,1,3,None, None,2]
val = 5
test = Solution()
root = test.buildBinaryTree(nums)
root = test.insertIntoMaxTree(root, val)
test.preOrder(root)
