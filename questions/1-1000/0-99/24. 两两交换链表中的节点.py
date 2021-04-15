# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
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
            print(head.val, end=' ')
            head = head.next
        print()

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = head.next
        head.next = self.swapPairs(last.next)
        last.next = head
        return last

nums = [1, 2, 3, 4]
test = Solution()
head = test.build(nums)
test.Print(head)
head = test.swapPairs(head)
test.Print(head)
