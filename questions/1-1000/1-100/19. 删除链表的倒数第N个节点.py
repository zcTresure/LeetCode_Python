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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, fast = dummy, head
        while n:
            n -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            head = head.next
            pre = pre.next
        pre.next = head.next
        return dummy.next


nums = [1, 2, 3, 4, 5]
n = 2
test = Solution()
head = test.build(nums)
head = test.removeNthFromEnd(head, n)
test.Print(head)
