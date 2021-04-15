# File Name:  105. 从前序与中序遍历序列构造二叉树
# date:       2021/3/29
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {val: i for i, val in enumerate(inorder)}

        def heaper(p_left, p_right, i_left, i_right):
            if p_left > p_right:
                return None
            # 在中序遍历中定位根节点
            i_root = index[preorder[p_left]]
            # # 前序遍历中的第一个节点就是根节点
            root = TreeNode(preorder[p_left])
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = heaper(p_left + 1, p_left + i_root - i_left, i_left, i_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = heaper(p_left + i_root - i_left + 1, p_right, i_root + 1, i_right)
            return root

        return heaper(0, n - 1, 0, n - 1)

    # 迭代
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root

    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
test = Solution()
root = test.buildTree(preorder, inorder)
test.preOrder(root)
