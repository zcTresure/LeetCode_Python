# File Name:  889. 根据前序和后序遍历构造二叉树
# date:       2021/4/3
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:])
        return root


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
test = Solution()
root = test.constructFromPrePost(pre, post)
test.levelOrder(root)
