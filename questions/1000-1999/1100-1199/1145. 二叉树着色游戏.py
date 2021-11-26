# File Name:  1145. 二叉树着色游戏
# date:       2021/3/31
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # 记录红点的左、右子树节点数目
        self.red_left, self.red_right = 0, 0

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == x:
                self.red_left = left
                self.red_right = right
            return left + right + 1

        dfs(root)
        # 记录根节点到红点的父节点和根节点另外一颗子树的节点树
        parent = n - self.red_left - self.red_right - 1
        judge = [parent, self.red_left, self.red_right]
        # 蓝点所占的位置可以分为三块，只需要有一个地方节点数大于所有节点树一半就行
        return any(blue > n // 2 for blue in judge)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 11
x = 1
test = Solution()
root = BinaryTree.build(nums)
print(test.btreeGameWinningMove(root, n, x))
