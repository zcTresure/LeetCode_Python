# File Name:  剑指 Offer 37. 序列化二叉树
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
    # 层次遍历
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

    # 序列化二叉树
    def serialize(self, root: TreeNode):
        if not root: return "[]"
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    # 反序列化二叉树
    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


nums = [1, 2, 3, None, None, 4, 5]
test = Codec()
root = BinaryTree.build(nums)
test.levelOrder(root)
data = test.serialize(root)
print(data)
root = test.deserialize(data)
test.levelOrder(root)
