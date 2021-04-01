# File Name:  894. 所有可能的满二叉树
# date:       2021/4/1
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    # 子问题：构造一棵满二叉树
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N == 1: return [TreeNode(0)]
        if N % 2 == 0: return []  # 结点个数必须是奇数
        left_num = 1  # 左子树分配一个节点
        right_num = N - 2  # 右子树可以分配到 N - 1 - 1 = N - 2 个节点
        while right_num > 0:
            left_tree = self.allPossibleFBT(left_num)  # 递归构造左子树
            right_tree = self.allPossibleFBT(right_num)  # 递归构造右子树
            for i in range(len(left_tree)):  # 具体构造过程
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
            left_num += 2  # 下一颗二叉树左子树加两个节点
            right_num -= 2  # 下一颗二叉树右子树减两个节点
        return res


n = 7
test = Solution()
asd = test.allPossibleFBT(n)
for i in range(len(asd)):
    print(test.preOrder(asd[i]))
