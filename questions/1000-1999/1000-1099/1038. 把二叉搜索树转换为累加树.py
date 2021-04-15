# File Name:  1038. 把二叉搜索树转换为累加树
# date:       2021/4/14
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
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(
                    nums[index]) if nums[index] != None else None
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

    # 反向中序遍历
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal tmp
            if root:
                dfs(root.right)
                tmp += root.val
                root.val = tmp
                dfs(root.left)

        tmp = 0
        dfs(root)
        return root

    # Morris 遍历
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node: TreeNode) -> TreeNode:
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ

        tmp = 0
        node = root
        while node:
            if not node.right:
                tmp += node.val
                node.val = tmp
                node = node.left
            else:
                succ = getSuccessor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    tmp += node.val
                    node.val = tmp
                    node = node.left
            if node:
                print(node.val, end=' ')
        print()
        return root

    # 层次遍历
    def levelorderPrint(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
        print()


nums = [4, 3, 5, 1, 2, 6, 8, None, None, None, None, None, None, 7]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
test.levelorderPrint(root)
test.bstToGst(root)
test.levelorderPrint(root)
