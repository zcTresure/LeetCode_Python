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

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    # 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous


nums = [1, 2, 3, 4]
test = Solution()
head = test.build(nums)
test.Print(head)
