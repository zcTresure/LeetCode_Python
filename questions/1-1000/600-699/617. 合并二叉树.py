import collections
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 深度优先搜索
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        merge = TreeNode(t1.val + t2.val)
        merge.left = self.mergeTrees(t1.left, t2.left)
        merge.right = self.mergeTrees(t1.right, t2.right)
        return merge

    # 广度优先搜索
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        merge = TreeNode(t1.val + t2.val)
        queue = collections.deque([merge])
        queue1 = collections.deque([t1])
        queue2 = collections.deque([t2])
        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.left or node2.left:
                if node1.left and node2.left:
                    left = TreeNode(node1.left.val + node2.left.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                elif node1.left:
                    node.left = node1.left
                elif node2.left:
                    node.left = node2.left
            if node1.right or node2.right:
                if node1.right and node2.right:
                    right = TreeNode(node1.right.val + node2.right.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                elif node1.right:
                    node.right = node1.right
                elif node2.right:
                    node.right = node2.right
        return merge


test = Solution()
nums1 = [1, 3, 2, 5]
nums2 = [2, 1, 3, None, 4, None, 7]
root1 = BinaryTree.build(nums1)
root2 = BinaryTree.build(nums2)
root = test.mergeTrees(root1, root2)
BinaryTree.levelOrder(root)
