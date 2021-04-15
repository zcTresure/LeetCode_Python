# File Name:  865. 具有所有最深节点的最小子树
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import namedtuple


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

    # 两次深度优先搜索
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}  # 记录每个节点的深度

        def dfs(node, parent=None):  # 根节点的父节点为空
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        max_depth = max(depth.values())  # 最深的节点

        def answer(node):
            # 该节点为空或者深度到达最大时返回
            if not node or depth.get(node) == max_depth:
                return node
            # 递归寻找左孩子 右孩子
            L, R = answer(node.left), answer(node.right)
            # 如果左右孩子节点都不为空，则返回该节点，否者返回左右孩子节点中的一个
            return node if L and R else L or R

        return answer(root)

    # 一次深度优先搜索
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 定义一个 Result 类，有 node 和 depth 属性
        Result = namedtuple("Result", ("node", "depth"))

        def dfs(node):
            if not node: return Result(None, 0)  # 如果节点为空，返回空节点和深度0
            L, R = dfs(node.left), dfs(node.right)  # 否则递归访问左右孩子节点
            if L.depth > R.depth: return Result(L.node, L.depth + 1)  # 左孩子深度大于右孩子深度时返回左孩子，并且深度加1
            if L.depth < R.depth: return Result(R.node, R.depth + 1)  # 右孩子深度大于左孩子深度时返回右孩子，并且深度加1
            return Result(node, L.depth + 1)

        return dfs(root).node  # 返回类 Result 的 node 属性


nums = [0, 1, 3, None, 2]
test = Solution()
root = test.buildBinaryTree(nums)
root = test.subtreeWithAllDeepest(root)
test.preOrder(root)
