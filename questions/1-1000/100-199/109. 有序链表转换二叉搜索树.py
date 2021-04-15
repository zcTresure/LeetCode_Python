import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一：分治
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

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return TreeNode(-1)
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        return buildTree(head, None)

    # 方法二：分治 + 中序遍历优化
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)

    def levelorderPrint(self, root: TreeNode) -> None:
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
        print()


nums = [-10, -3, 0, 5, 9]
test = Solution()
link = test.build(nums)
root = test.sortedListToBST(link)
test.levelorderPrint(root)
