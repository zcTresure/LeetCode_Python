# File Name:  1110. 删点成林
# date:       2021/3/29
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
    # 先序遍历
    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return []  # 根节点为空， 直接返回
        dir = set(to_delete)  # 去除 to_delete 中重复的元素
        ans = [] if root.val in dir else [root]  # 判断根节点是否要删除

        # parent 为父节点 direction 标记父节点的左或右孩子为 node
        def dfs(node, parent, direction):
            if not node: return  # 节点为空直接返回
            dfs(node.left, node, 'left')
            dfs(node.right, node, 'right')
            if node.val in dir:  # 节点值在 to_delete 中进行处理
                if node.left: ans.append(node.left)  # 节点左孩子存在，加入数组
                if node.right: ans.append(node.right)  # 节点右孩子存在，加入数组
                if direction == 'left': parent.left = None
                if direction == 'right': parent.right = None

        dfs(root, None, None)
        return ans


nums = [1, 2, 3, 4, 5, 6, 7]
to_delete = [3, 5]
test = Solution()
root = BinaryTree.build(nums)
ret = test.delNodes(root, to_delete)
for i in range(len(ret)):
    test.preOrder(ret[i])
    print()
