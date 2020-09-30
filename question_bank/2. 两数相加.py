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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(None)
        tmp = 0
        while l1 or l2 or tmp:
            tmp += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(tmp % 10)
            cur = cur.next
            tmp //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()


nums1 = [3, 2, 4]
nums2 = [4, 5, 6]
test = Solution()
l1 = test.build(nums1)
l2 = test.build(nums2)
s = test.addTwoNumbers(l1, l2)
test.Print(s)
