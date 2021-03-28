# File Name:  面试题 04.05. 合法二叉搜索树
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'


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

    # 递归
    def isValidBST(self, root: TreeNode) -> bool:
        def heaper(node, left=-float('inf'), right=float('inf')):
            if not node: return True
            if node.val <= left or node.val >= right:
                return False
            if not heaper(node.left, left, node.val):
                return False
            if not heaper(node.right, node.val, right):
                return False
            return True

        return heaper(root)

    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], -float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:  # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
                return False
            inorder = root.val
            root = root.right
        return True


nums = [2, 1, 3]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.isValidBST(root))
