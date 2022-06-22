# File Name:  513. 找树左下角的值
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from typing import Optional
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.val = root.val if root else 0  # 记录最深层最左边节点的值
        self.cur_max_depth = -1  # 记录树的最深层树，默认-1为空树

        def heaper(node, depth=0):
            if not node: return
            if depth > self.cur_max_depth:
                self.cur_max_depth = depth  # 更新树的层数
                self.val = node.val  # 更新最左节点值
            heaper(node.left, depth + 1)  # 递归
            heaper(node.right, depth + 1)

        heaper(root)
        return self.val

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    ans = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans


nodes = [1, 2, 3, 4, 5, 6, None, None, 7]
test = Solution()
root = BinaryTree.build(nodes)
print(test.findBottomLeftValue(root))
