# File Name:  297. 二叉树的序列化与反序列化
# date:       2021/4/3
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def levelOrder(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                print(node.val, end='')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q:
                    print(end=' ')
        print()

    def serialize(self, root: TreeNode):
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append("#")

        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "#": return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(","))
        return dfs()


nums = [1, 2, 3, None, None, 4, 5]
test = Codec()
root = BinaryTree.build(nums)
test.levelOrder(root)
data = test.serialize(root)
print(data)
root = test.deserialize(data)
test.levelOrder(root)
