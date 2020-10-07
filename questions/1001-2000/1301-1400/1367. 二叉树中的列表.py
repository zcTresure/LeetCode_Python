import collections


# Definition for a binary tree node.
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
    def build(self, nums: list) -> ListNode:
        if not nums:
            return
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

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
link = test.build(head)
root = test.constructTreeNodeDynamic(nums)
print(test.isSubPath(link, root))
