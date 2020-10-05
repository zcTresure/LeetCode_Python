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

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        pre, dummy.next = dummy, head
        while head:
            if head.val == val:
                pre.next = head.next
                del head
                return dummy.next
            pre, head = pre.next, head.next

nums = [2,0,1,3]
val = 0
test = Solution()
head = test.build(nums)
head = test.deleteNode(head,val)
test.Print(head)