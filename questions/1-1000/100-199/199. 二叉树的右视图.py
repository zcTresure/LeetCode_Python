# File Name:  199. 二叉树的右视图
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []  # 没有根节点，直接输出
        res = []  # 记录从根节点到最深叶子节点的最右侧节点值
        que = [root]  # 将根节点入数组
        while que:  # 数组为空时 则到了最后一层，直接退出
            res.append(que[-1].val)  # 记录每一层最右节点值
            tmp = []  # 下一层节点从左到右记录
            for i in range(len(que)):
                node = que[i]
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            que = tmp  # 更新当前层
        return res


nums = [1, 2, 3, None, 5, None, 4]
test = Solution()
root = BinaryTree.build(nums)
print(test.rightSideView(root))
