# Definition for a binary tree node.
import BinaryTree
import LinkList


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def dfs(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


head = [4, 2, 8]
nums = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
test = Solution()
link = LinkList.build(head)
root = BinaryTree.build(nums)
print(test.isSubPath(link, root))
