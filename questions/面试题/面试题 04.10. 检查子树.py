# File Name:  面试题 04.10. 检查子树
# date:       2021/4/16
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
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(t1, t2):
            if t1 == t2: return True
            if not t1 or not t2: return False
            return t1.val == t2.val and dfs(t1.left, t2.left) and dfs(t1.right, t2.right)

        if not t2: return True
        if not t1: return False
        return dfs(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def preorder(node, nums):  # 先序遍历序列化节点
            if not node: return
            nums.append(node.val)
            preorder(node.left, nums)
            preorder(node.right, nums)

        def kmp(origin, match, next):  # kmp字符串匹配算法
            len1, len2 = len(origin), len(match)
            if len1 < len2: return False
            i1 = i2 = 0
            while i1 < len1 and i2 < len2:
                if origin[i1] == match[i2]:
                    i1 += 1
                    i2 += 1
                elif next[i2] == -1:
                    i1 += 1
                else:
                    i2 = next[i2]
            return True if i2 == len(match) else False

        def getNext(match):  # 获取kmp算法的next数组
            n = len(match)
            if n == 1: return [-1]
            next = [-1] + [0] * (n - 1)
            pre_next, curr = 0, 2
            while curr < n:
                if match[pre_next] == match[curr]:
                    pre_next += 1
                    next[curr] = pre_next
                    curr += 1
                elif pre_next > 0:
                    pre_next = next[pre_next]
                else:
                    next[curr] = 0
                    curr += 1
            return next

        if not t2: return True
        if not t1: return False
        origin, match = [], []
        preorder(t1, origin)
        preorder(t2, match)
        next = getNext(match)
        print(origin)
        print(match)
        print(next)

        return kmp(origin, match, next)


t1 = [1, 2, 3, 4, 2, None, None, 4, 2, 4, 2]
t2 = [2, 4, 2, 4, 2, 4, 2]
test = Solution()
root1 = BinaryTree.build(t1)
root2 = BinaryTree.build(t2)
print(test.checkSubTree(root1, root2))
